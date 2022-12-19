from pydantic import BaseModel
from typing import List
from api.model.modelMessage import MessageOut

class Messages(BaseModel):
    Messages: list[MessageOut]
    count: int
