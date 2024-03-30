from fastapi import FastAPI, Depends
from auth import authenticate

app = FastAPI(dependencies=[Depends(authenticate)])

@app.get("/test")
async def get_route():
    return "Hello friend!"