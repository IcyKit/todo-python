from pydantic import BaseModel


class ToDoCreate(BaseModel):
    title: str
    description: str


class ToDoType(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
