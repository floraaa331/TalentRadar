# TalentRadar

AI-powered job market analytics dashboard. Paste a job description — get skills, seniority, salary estimates, and market demand analysis.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Frontend (React)                  │
│  ┌──────────┐  ┌────────────┐  ┌─────────────────┐  │
│  │ Analyze  │  │  Results   │  │    History       │  │
│  │  Form    │  │ Dashboard  │  │  + Stats Charts  │  │
│  └────┬─────┘  └─────▲──────┘  └───────▲─────────┘  │
│       │              │                  │            │
└───────┼──────────────┼──────────────────┼────────────┘
        │ POST         │ JSON             │ GET
        ▼              │                  │
┌───────┴──────────────┴──────────────────┴────────────┐
│                Backend (FastAPI)                      │
│  ┌────────────┐  ┌────────────┐  ┌────────────────┐  │
│  │ /analysis  │  │  /history  │  │  /history/stats│  │
│  └─────┬──────┘  └─────┬──────┘  └───────┬────────┘  │
│        │               │                 │           │
│   ┌────▼────┐     ┌────▼──────────────────▼────┐     │
│   │   AI    │     │        PostgreSQL          │     │
│   │ Service │     │    (job_analyses table)     │     │
│   └────┬────┘     └────────────────────────────┘     │
│        │                                             │
│   ┌────▼────┐     ┌──────────────────┐               │
│   │Anthropic│     │      Redis       │               │
│   │  API    │     │  (analysis cache)│               │
│   └─────────┘     └──────────────────┘               │
└──────────────────────────────────────────────────────┘
```

## Tech Stack

| Layer    | Technology                          |
|----------|-------------------------------------|
| Frontend | React 18, React Router, Recharts    |
| Backend  | Python 3.12, FastAPI, SQLAlchemy    |
| Database | PostgreSQL 16                       |
| Cache    | Redis 7                             |
| AI       | Anthropic Claude (claude-sonnet-4-20250514) |
| Deploy   | Docker, docker-compose, Railway     |

## Quick Start

### Docker (recommended)

```bash
# 1. Clone and enter the project
cd TalentRadar

# 2. Set your Anthropic API key
export ANTHROPIC_API_KEY=sk-ant-your-key-here

# 3. Start everything
cd docker
docker-compose up --build

# 4. Open http://localhost in your browser
```

### Local Development

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Set environment variables (or create .env from .env.example)
export DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/talentradar
export REDIS_URL=redis://localhost:6379/0
export ANTHROPIC_API_KEY=sk-ant-your-key-here

uvicorn app.main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
REACT_APP_API_URL=http://localhost:8000/api npm start
```

### Railway Deployment

1. Push the repo to GitHub
2. Connect to Railway
3. Add PostgreSQL and Redis plugins
4. Set `ANTHROPIC_API_KEY` in environment variables
5. Deploy — `railway.json` handles the rest

## API Endpoints

| Method | Endpoint          | Description                    |
|--------|-------------------|--------------------------------|
| POST   | /api/analysis/    | Analyze a job description      |
| GET    | /api/history/     | Get last N analyzed jobs       |
| GET    | /api/history/stats| Aggregate skill/stack stats    |
| GET    | /api/health       | Health check                   |
| GET    | /docs             | OpenAPI interactive docs       |

## Features

- **AI Analysis** — extracts skills, seniority, tech stack, salary range, and market demand score
- **Visual Dashboard** — bar charts, gauge, salary cards, skill tags with Recharts
- **History & Stats** — browse past analyses with aggregate charts
- **Redis Caching** — identical descriptions return cached results
- **Dark/Light Theme** — toggle with persistence
- **Mobile Responsive** — works on all screen sizes
- **Seed Data** — 3 example analyses loaded on first run
