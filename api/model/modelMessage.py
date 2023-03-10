from pydantic import BaseModel, Field
from typing import Optional
from itertools import count


c = count()


class MessageOut(BaseModel):
    id: Optional[int]
    text: str
    votes: Optional[int] = 0


class MessageIn(BaseModel):
    text: str


class MessageRandom(BaseModel):
    votes: Optional[int] = 0
