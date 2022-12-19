from pydantic import BaseModel, Field
from typing import Optional
from itertools import count


c = count()


class MessageOut(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
    text: str
    votes: Optional[int] = 0

class MessageIn(BaseModel):
    text: str