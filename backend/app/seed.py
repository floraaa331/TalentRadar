import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import JobAnalysis

SEED_DATA = [
    {
        "job_description": "Senior Python Developer needed for fintech startup. Requirements: 5+ years Python, FastAPI or Django, PostgreSQL, Redis, Docker, Kubernetes. Experience with microservices architecture, CI/CD pipelines, and AWS. Nice to have: Go, GraphQL, machine learning basics. Remote-friendly, competitive salary.",
        "skills": [
            {"name": "Python", "category": "language", "importance": "must"},
            {"name": "FastAPI", "category": "framework", "importance": "must"},
            {"name": "Django", "category": "framework", "importance": "must"},
            {"name": "PostgreSQL", "category": "database", "importance": "must"},
            {"name": "Redis", "category": "database", "importance": "must"},
            {"name": "Docker", "category": "tool", "importance": "must"},
            {"name": "Kubernetes", "category": "tool", "importance": "must"},
            {"name": "AWS", "category": "cloud", "importance": "must"},
            {"name": "Go", "category": "language", "importance": "nice"},
            {"name": "GraphQL", "category": "framework", "importance": "nice"},
            {"name": "Machine Learning", "category": "other", "importance": "nice"},
        ],
        "seniority": "senior",
        "stack_tags": ["Python", "Backend", "Cloud", "DevOps", "Fintech"],
        "market_demand_score": 8.5,
        "salary_min": 250000,
        "salary_max": 400000,
        "summary": "High-demand senior backend role in fintech. Strong Python ecosystem with cloud-native requirements. The microservices and K8s focus signals a mature engineering org with competitive compensation.",
    },
    {
        "job_description": "Middle Frontend Developer — React, TypeScript. We are looking for an experienced frontend developer to join our e-commerce team. Must know: React 18+, TypeScript, Redux Toolkit, REST API integration, responsive design. Nice to have: Next.js, testing (Jest, RTL), Storybook, Figma. Hybrid office in Moscow.",
        "skills": [
            {"name": "React", "category": "framework", "importance": "must"},
            {"name": "TypeScript", "category": "language", "importance": "must"},
            {"name": "Redux Toolkit", "category": "framework", "importance": "must"},
            {"name": "REST API", "category": "other", "importance": "must"},
            {"name": "Responsive Design", "category": "other", "importance": "must"},
            {"name": "Next.js", "category": "framework", "importance": "nice"},
            {"name": "Jest", "category": "tool", "importance": "nice"},
            {"name": "Storybook", "category": "tool", "importance": "nice"},
            {"name": "Figma", "category": "tool", "importance": "nice"},
        ],
        "seniority": "mid",
        "stack_tags": ["React", "Frontend", "TypeScript", "E-commerce"],
        "market_demand_score": 7.0,
        "salary_min": 150000,
        "salary_max": 250000,
        "summary": "Standard mid-level React position in e-commerce. The TypeScript + Redux Toolkit combo is market-standard. Hybrid Moscow office may limit candidate pool but the stack is mainstream.",
    },
    {
        "job_description": "Junior Data Analyst. Join our analytics team! Requirements: SQL basics, Python (pandas, numpy), Excel/Google Sheets, basic statistics knowledge. Will be great if you know: Tableau or Power BI, A/B testing, basic ML concepts. We provide mentorship and training. Full-time, office in Saint Petersburg.",
        "skills": [
            {"name": "SQL", "category": "language", "importance": "must"},
            {"name": "Python", "category": "language", "importance": "must"},
            {"name": "Pandas", "category": "framework", "importance": "must"},
            {"name": "NumPy", "category": "framework", "importance": "must"},
            {"name": "Excel", "category": "tool", "importance": "must"},
            {"name": "Statistics", "category": "other", "importance": "must"},
            {"name": "Tableau", "category": "tool", "importance": "nice"},
            {"name": "Power BI", "category": "tool", "importance": "nice"},
            {"name": "A/B Testing", "category": "methodology", "importance": "nice"},
        ],
        "seniority": "junior",
        "stack_tags": ["Python", "Data", "Analytics", "SQL"],
        "market_demand_score": 6.0,
        "salary_min": 60000,
        "salary_max": 100000,
        "summary": "Entry-level data analyst role with mentorship. Standard analytics stack with Python and SQL focus. The mentorship offer and basic requirements make this ideal for career starters in data.",
    },
]


async def seed_database(db: AsyncSession):
    result = await db.execute(select(JobAnalysis).limit(1))
    if result.scalars().first() is not None:
        return

    for i, data in enumerate(SEED_DATA):
        record = JobAnalysis(
            job_description=data["job_description"],
            skills=data["skills"],
            seniority=data["seniority"],
            stack_tags=data["stack_tags"],
            market_demand_score=data["market_demand_score"],
            salary_min=data["salary_min"],
            salary_max=data["salary_max"],
            summary=data["summary"],
            created_at=datetime.datetime.utcnow() - datetime.timedelta(hours=i * 2),
        )
        db.add(record)

    await db.commit()
