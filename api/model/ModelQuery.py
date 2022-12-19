from typing import Optional
from pydantic import BaseModel, Field


class QueryMessage(BaseModel):
    id: Optional[int]
    text: Optional[str]
    votes: Optional[int]


class QueryUpdate(BaseModel):
    id: int
