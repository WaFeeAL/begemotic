from functools import lru_cache

from apps.core.config import Settings


@lru_cache
def get_settings() -> Settings:
    return Settings()
