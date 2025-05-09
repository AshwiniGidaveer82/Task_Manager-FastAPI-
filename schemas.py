from pydantic import BaseModel
from typing import Optional

# Schema for creating a task
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

# Schema for updating a task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
