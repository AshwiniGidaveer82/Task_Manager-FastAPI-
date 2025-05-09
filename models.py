from pydantic import BaseModel
from typing import Optional

# Pydantic model for Task
class TaskDB(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

    class Config:
        orm_mode = True
