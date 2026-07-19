
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

    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "rashno"
    POSTGRES_PASS: str 
    POSTGRES_DB: str = "vending" 
    DATABASE_URL: str | None = None

    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str | None = None 

    def REDIS_URL(self) -> str:
        auth = f":{self.REDIS_PASSWORD}@" if self.REDIS_PASSWORD else ""
        return f"redis://{auth}{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"


    def database_url_async(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASS}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


@lru_cache
def get_settings() -> Settings:
    """Singleton settings — read once, reused everywhere."""
    return Settings()  # type: ignore[call-arg]


config = get_settings()
