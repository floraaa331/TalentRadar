from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import JobAnalysis
from app.schemas import AnalysisRequest, JobAnalysisResponse, AnalysisResult, SalaryRange, Skill
from app.services.ai_service import analyze_job_description
from app.services.cache_service import get_cached_analysis, set_cached_analysis

router = APIRouter(prefix="/api/analysis", tags=["analysis"])


def _model_to_response(record: JobAnalysis) -> JobAnalysisResponse:
    return JobAnalysisResponse(
        id=record.id,
        job_description=record.job_description,
        skills=[Skill(**s) for s in record.skills],
        seniority=record.seniority,
        stack_tags=record.stack_tags,
        market_demand_score=record.market_demand_score,
        salary_range_rub=SalaryRange(min=record.salary_min, max=record.salary_max),
        summary=record.summary,
        created_at=record.created_at,
    )


@router.post("/", response_model=JobAnalysisResponse)
async def analyze(request: AnalysisRequest, db: AsyncSession = Depends(get_db)):
    cached = await get_cached_analysis(request.job_description)
    if cached:
        result = AnalysisResult(**cached)
    else:
        try:
            result = await analyze_job_description(request.job_description)
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"AI analysis failed: {str(e)}")
        await set_cached_analysis(request.job_description, result.model_dump())

    record = JobAnalysis(
        job_description=request.job_description,
        skills=[s.model_dump() for s in result.skills],
        seniority=result.seniority,
        stack_tags=result.stack_tags,
        market_demand_score=result.market_demand_score,
        salary_min=result.salary_range_rub.min,
        salary_max=result.salary_range_rub.max,
        summary=result.summary,
    )
    db.add(record)
    await db.commit()
    await db.refresh(record)

    return _model_to_response(record)
