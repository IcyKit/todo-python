from typing import Optional
from pydantic import BaseModel


class ToDoCreate(BaseModel):
    title: str
    description: str


class ToDoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class ToDoType(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
