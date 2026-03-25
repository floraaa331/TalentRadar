import hashlib
import json
from app.redis_client import redis_client
from app.config import get_settings

settings = get_settings()


def _cache_key(job_description: str) -> str:
    h = hashlib.sha256(job_description.strip().lower().encode()).hexdigest()[:16]
    return f"talentradar:analysis:{h}"


async def get_cached_analysis(job_description: str) -> dict | None:
    try:
        key = _cache_key(job_description)
        data = await redis_client.get(key)
        if data:
            return json.loads(data)
    except Exception:
        pass
    return None


async def set_cached_analysis(job_description: str, result: dict) -> None:
    try:
        key = _cache_key(job_description)
        await redis_client.setex(key, settings.cache_ttl_seconds, json.dumps(result))
    except Exception:
        pass
