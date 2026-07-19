from fastapi import FastAPI 
from app.core.logger import get_logger 
import asyncio 

from contextlib import asynccontextmanager 
from app.database.session import check_db_connection, async_engine 
from app.database.redis import close_redis , get_redis


logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app : FastAPI) : 
    logger.info(
        "app starting ..."
    )

    db_ok = await check_db_connection() 

    if not db_ok : 
        logger.error(
            "database is not ok"
        )

    else : 
        logger.info(
            "database is ok"
        )

    try:
        await get_redis().ping()
        logger.info("startup_redis_ok")
    except Exception as exc:
        logger.error("startup_redis_unreachable", err=str(exc))



    yield

    logger.info(
        "shutting down server ... "
    )

    await async_engine.dispose() 

app = FastAPI(
    lifespan=lifespan
) 
    


@app.get("/")
def main() : 
    return {"details" : "welcome"}