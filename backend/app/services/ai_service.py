import json
from groq import AsyncGroq
from app.config import get_settings
from app.schemas import AnalysisResult

settings = get_settings()

ANALYSIS_PROMPT = """Analyze the following job description and return a structured JSON response.

Return ONLY valid JSON with this exact structure (no markdown, no code fences):
{
  "skills": [{"name": "skill name", "category": "category", "importance": "must or nice"}],
  "seniority": "junior or mid or senior",
  "stack_tags": ["tag1", "tag2"],
  "market_demand_score": <number 1-10>,
  "salary_range_rub": {"min": <number>, "max": <number>},
  "summary": "2-3 sentence analysis"
}

Rules:
- "importance" must be exactly "must" or "nice"
- "seniority" must be exactly "junior", "mid", or "senior"
- "market_demand_score" is 1-10 based on current market demand
- "salary_range_rub" is monthly salary in Russian rubles
- "skills" should include all mentioned technical and soft skills
- "stack_tags" are high-level technology categories
- "category" for skills: "language", "framework", "database", "cloud", "tool", "soft_skill", "methodology", "other"

Job description:
"""


async def analyze_job_description(text: str) -> AnalysisResult:
    client = AsyncGroq(api_key=settings.groq_api_key)

    message = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=2048,
        messages=[
            {"role": "user", "content": ANALYSIS_PROMPT + text}
        ],
    )

    raw = message.choices[0].message.content.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()

    data = json.loads(raw)
    return AnalysisResult(**data)
