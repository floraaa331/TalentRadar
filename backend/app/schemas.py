from pydantic import BaseModel, Field
from datetime import datetime


class Skill(BaseModel):
    name: str
    category: str
    importance: str = Field(pattern=r"^(must|nice)$")


class SalaryRange(BaseModel):
    min: int
    max: int


class AnalysisRequest(BaseModel):
    job_description: str = Field(min_length=20, max_length=10000)


class AnalysisResult(BaseModel):
    skills: list[Skill]
    seniority: str
    stack_tags: list[str]
    market_demand_score: float = Field(ge=1, le=10)
    salary_range_rub: SalaryRange
    summary: str


class JobAnalysisResponse(BaseModel):
    id: int
    job_description: str
    skills: list[Skill]
    seniority: str
    stack_tags: list[str]
    market_demand_score: float
    salary_range_rub: SalaryRange
    summary: str
    created_at: datetime

    model_config = {"from_attributes": True}
