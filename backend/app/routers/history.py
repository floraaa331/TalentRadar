from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import JobAnalysis
from app.schemas import JobAnalysisResponse, SalaryRange, Skill

router = APIRouter(prefix="/api/history", tags=["history"])


@router.get("/", response_model=list[JobAnalysisResponse])
async def get_history(limit: int = 10, db: AsyncSession = Depends(get_db)):
    stmt = select(JobAnalysis).order_by(JobAnalysis.created_at.desc()).limit(limit)
    result = await db.execute(stmt)
    records = result.scalars().all()

    return [
        JobAnalysisResponse(
            id=r.id,
            job_description=r.job_description,
            skills=[Skill(**s) for s in r.skills],
            seniority=r.seniority,
            stack_tags=r.stack_tags,
            market_demand_score=r.market_demand_score,
            salary_range_rub=SalaryRange(min=r.salary_min, max=r.salary_max),
            summary=r.summary,
            created_at=r.created_at,
        )
        for r in records
    ]


@router.get("/stats")
async def get_stats(db: AsyncSession = Depends(get_db)):
    stmt = select(JobAnalysis).order_by(JobAnalysis.created_at.desc()).limit(100)
    result = await db.execute(stmt)
    records = result.scalars().all()

    skill_freq: dict[str, int] = {}
    stack_freq: dict[str, int] = {}
    seniority_count: dict[str, int] = {}

    for r in records:
        for skill in r.skills:
            name = skill["name"]
            skill_freq[name] = skill_freq.get(name, 0) + 1
        for tag in r.stack_tags:
            stack_freq[tag] = stack_freq.get(tag, 0) + 1
        seniority_count[r.seniority] = seniority_count.get(r.seniority, 0) + 1

    top_skills = sorted(skill_freq.items(), key=lambda x: x[1], reverse=True)[:15]
    top_stacks = sorted(stack_freq.items(), key=lambda x: x[1], reverse=True)[:10]

    return {
        "total_analyses": len(records),
        "top_skills": [{"name": n, "count": c} for n, c in top_skills],
        "top_stacks": [{"name": n, "count": c} for n, c in top_stacks],
        "seniority_distribution": seniority_count,
    }
