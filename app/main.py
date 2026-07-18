from fastapi import FastAPI 

import asyncio 

app = FastAPI() 


@app.get("/")
def main() : 
    return {"details" : "welcome"}