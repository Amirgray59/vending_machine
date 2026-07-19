from sqlalchemy.ext.asyncio import (
    AsyncSession , 
    async_sessionmaker , 
    create_async_engine 
)

from sqlalchemy.orm import DeclarativeBase 

from app.core.config import config 

async_engine = create_async_engine(
    config.database_url_async(), 
    echo=False , 
    pool_pre_ping=True
)


async_session_maker = async_sessionmaker(
    bind=async_engine
)

async def get_db() -> AsyncSession : 
    async with async_session_maker() as session : 
        yield session 


async def check_db_connection() -> bool:
    from sqlalchemy import text

    try:
        async with async_engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return True
    except Exception as exc:  # pragma: no cover
        log.error("db_connection_failed", err=str(exc))
        return False
