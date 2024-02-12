from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.models import UUIDModel, TimestampModel
  

class GameBase(SQLModel):  
    name: str = None
    description: str = None
    price: int | None = 0

class Game(GameBase, UUIDModel, TimestampModel, table=True):
    __tablename__ = "games"

class GameCreate(GameBase):  
    pass  
  
class GameUpdate(GameBase):  
    name: str | None = None
    description: str | None = None 
    price: int | None = None

