from sqlmodel import SQLModel, Relationship
from src.models import UUIDModel, TimestampModel, GamePlatformLink

from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
  from src.games.models import Game


class PlatformBase(SQLModel):  
    name: str = None
    company: str = None
    

class Platform(PlatformBase, UUIDModel, TimestampModel, table=True):
    __tablename__ = "platforms"
    games: List["Game"] = Relationship(back_populates="platforms", link_model=GamePlatformLink)
