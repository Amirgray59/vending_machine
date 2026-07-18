
from pydantic_settings import BaseSettings , SettingsConfigDict 

from functools import lru_cache

class Settings(BaseSettings) : 
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    API_HOST : str = "0.0.0.0"
    API_PORT: int = 8000

    TCP_HOST : str = "0.0.0.0"
    TCP_PORT : int = 9000 



@lru_cache
def get_settings() -> Settings:
    """Singleton settings — read once, reused everywhere."""
    return Settings()  # type: ignore[call-arg]


config = get_settings()
