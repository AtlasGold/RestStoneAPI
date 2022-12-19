from pydantic import BaseModel, Field
from typing import Optional
from itertools import count


c = count()


class Message(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
    text: str
    votes: int