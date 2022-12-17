from pydantic import BaseModel
from typing import Optional
from typing import List
from model.modelMessage import Message

class Messages(BaseModel):
    Messages: list[Message]
    count: int
