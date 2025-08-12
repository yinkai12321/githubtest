import os
import redis.asyncio as redis


REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")


def get_redis() -> redis.Redis:
    """Return a Redis client instance."""
    return redis.from_url(REDIS_URL)
