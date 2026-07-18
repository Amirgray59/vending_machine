from fastapi import FastAPI 
from app.hardware.server import HardwareGateway 
import asyncio 

app = FastAPI() 

gateway = HardwareGateway() 


@app.on_event("startup")
async def startup_server() : 
    asyncio.create_task(
        gateway.start()
    )    


@app.on_event("shutdown") 
async def shutdown_server() : 
    await gateway.shutdownD()
    

@app.get("/")
def main() : 
    return {"details" : "welcome"}