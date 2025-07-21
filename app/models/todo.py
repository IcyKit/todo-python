from sqlalchemy import Column, Integer, String, Boolean
from db.db import Base


class ToDo:
    def __init__(self, title: str, description: str, id: int, is_completed: bool = False,):
        self.title = title
        self.description = description
        self.is_completed = is_completed
        self.id = id

    def update(self, todo):
        if hasattr(todo, 'title') and todo.title is not None:
            self.title = todo.title

        if hasattr(todo, 'description') and todo.description is not None:
            self.description = todo.description

        if hasattr(todo, 'is_completed') and todo.is_completed is not None:
            self.is_completed = todo.is_completed

        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'is_completed': self.is_completed,
        }


class ToDoModel(Base):
    """Модель для взаимодействия с DB"""

    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False)
