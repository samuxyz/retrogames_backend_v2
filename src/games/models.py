from sqlmodel import SQLModel, Relationship
from src.models import UUIDModel, TimestampModel, GamePlatformLink
from typing import List, TYPE_CHECKING


if TYPE_CHECKING:
  from src.platforms.models import Platform
  
class GameBase(SQLModel):  
    name: str = None
    description: str = None
    price: int | None = 0
    

class Game(GameBase, UUIDModel, TimestampModel, table=True):
    __tablename__ = "games"
    platforms: List["Platform"] = Relationship(back_populates="games", link_model=GamePlatformLink)


class GameCreate(GameBase):  
    pass  
  
class GameUpdate(GameBase):  
    name: str | None = None
    description: str | None = None 
    price: int | None = None







