
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
    POSTGRES_PASS: str = "pTtQ3uU2_5bihS8xTxKV46zgfP9eE7z3"
    POSTGRES_DB: str = "vending"
    DATABASE_URL: str | None = None

    def database_url_async(self) -> str:
        """DSN async (asyncpg) — used by SQLAlchemy AsyncEngine."""
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


@lru_cache
def get_settings() -> Settings:
    """Singleton settings — read once, reused everywhere."""
    return Settings()  # type: ignore[call-arg]


config = get_settings()
