from sqlalchemy.ext.asyncio import (
    AsyncSession , 
    async_sessionmaker , 
    create_async_engine 
)

from sqlalchemy.orm import DeclarativeBase 

from app.core.config import config 

async_engine = create_async_engine(
    config.DATABASE_URL(), 
    echo=False , 
    pool_pre_ping=True
)


async_session_maker = async_sessionmaker(
    bind=async_engine
)

async def get_db() -> AsyncSession : 
    async with async_session_maker() as session : 
        yield session 