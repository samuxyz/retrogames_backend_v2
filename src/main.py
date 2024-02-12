from fastapi import FastAPI
from .games.router import router as games_router
from core.config import settings
from src.games.models import Game

app = FastAPI(
    title=settings.title,
    version=settings.version,
    description=settings.description,
    root_path=settings.openapi_prefix,
    docs_url=settings.docs_url,
    openapi_url=settings.openapi_url
)
app.include_router(
    games_router
)

@app.get("/")
async def index():
  return {"Welcome to Retrogames API"}

