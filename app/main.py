from fastapi import FastAPI 
from app.core.logger import get_logger 
import asyncio 

from contextlib import asynccontextmanager 
from app.database.session import check_db_connection

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


    yield

app = FastAPI(
    lifespan=lifespan
) 
    


@app.get("/")
def main() : 
    return {"details" : "welcome"}