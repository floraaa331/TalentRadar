from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.database import init_db, async_session
from app.routers import analysis, history
from app.seed import seed_database

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    async with async_session() as db:
        await seed_database(db)
    yield


app = FastAPI(
    title="TalentRadar API",
    description="AI-powered job market analytics",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis.router)
app.include_router(history.router)


@app.get("/api/health")
async def health_check():
    return {"status": "ok"}
