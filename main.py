from typing import Optional
from fastapi import FastAPI, Header
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="public", html=True), name="static")

@app.get("/items")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}