from fastapi import APIRouter, HTTPException, Depends
from .models import Game, GameCreate, GameUpdate
from sqlmodel import Session, select
from sqlmodel.ext.asyncio.session import AsyncSession
from src.database import get_session
from uuid import UUID

router = APIRouter(
    prefix="/games",
    tags=["games"]
)

@router.get("/", response_model = list[GameCreate])
async def getGames(db: AsyncSession = Depends(get_session)):
    result = await db.exec(select(Game))
    games = result.all()
    return games

@router.post("/", response_model = Game, status_code=201)
async def postGame(game: GameCreate, db: AsyncSession = Depends(get_session)) -> Game:
    game = Game(
        name=game.name,
        description=game.description,
        price=game.price
    )
    db.add(game)
    await db.commit()
    await db.refresh(game)
    return game

@router.get("/{game_id}", response_model = Game)  
async def getGame(game_id: UUID, db: AsyncSession = Depends(get_session)) -> Game:
    game = await db.get(Game, game_id)
    if not game:
        raise HTTPException(
            status_code=404,
            detail="Game not found"
        )
    return game


@router.delete("/{game_id}", response_model = Game)
async def deleteGame(game_id: UUID, db: AsyncSession = Depends(get_session)) -> Game:
    game = await db.get(Game, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    await db.delete(game)
    await db.commit()
    return game

@router.patch("/{game_id}", response_model=Game)
async def putGame(game_id: UUID, game: GameUpdate, db: AsyncSession = Depends(get_session)) -> Game:
    game_current = await db.get(Game, game_id)
    if not game_current:
        raise HTTPException(status_code=404, detail="Game not found")
    game_data = game.model_dump(exclude_unset=True)
    for key, value in game_data.items():
        setattr(game_current, key, value)
    db.add(game_current)
    await db.commit()
    await db.refresh(game_current)
    return game_current

