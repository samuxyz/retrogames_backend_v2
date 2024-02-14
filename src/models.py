from uuid import uuid4, UUID  
from datetime import datetime  
  
from sqlalchemy import text  
from sqlmodel import Field, SQLModel  
  
  
class UUIDModel(SQLModel):  
    id: UUID = Field(  
        default_factory=uuid4,  
        primary_key=True,  
        index=True,  
        nullable=False,  
    )  
  
  
class TimestampModel(SQLModel):  
    created_at: datetime = Field(  
        default_factory=datetime.utcnow,  
        nullable=False,  
        sa_column_kwargs={"server_default": text("current_timestamp(0)")},  
    )


class GamePlatformLink(SQLModel, table=True):
    __tablename__= "gamesplatforms"
    game_id: UUID =  Field(
        default=None, foreign_key="games.id", primary_key=True
    )
    platform_id: UUID = Field(
        default=None, foreign_key="platforms.id", primary_key=True
    )
