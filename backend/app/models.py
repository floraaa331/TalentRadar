import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, JSON
from app.database import Base


class JobAnalysis(Base):
    __tablename__ = "job_analyses"

    id = Column(Integer, primary_key=True, index=True)
    job_description = Column(Text, nullable=False)
    skills = Column(JSON, nullable=False, default=list)
    seniority = Column(String(20), nullable=False)
    stack_tags = Column(JSON, nullable=False, default=list)
    market_demand_score = Column(Float, nullable=False)
    salary_min = Column(Integer, nullable=True)
    salary_max = Column(Integer, nullable=True)
    summary = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
