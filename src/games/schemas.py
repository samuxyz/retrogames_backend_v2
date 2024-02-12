from pydantic import BaseModel 


class Game(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None


