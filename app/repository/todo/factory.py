from typing import Literal, Optional
from models.todo import ToDo
from repository.todo.todo_db_repository import ToDoDBRepository
from repository.todo.todo_memory_repository import ToDoMemoryRepository
from fastapi import Depends
from sqlalchemy.orm import Session
from db.db import get_db


def get_repo(repo: Literal["db", "memory"], db: Optional[Session] = None):
    if repo == "db":
        assert db is not None
        return ToDoDBRepository(db)
    elif repo == "memory":
        return ToDoMemoryRepository([
            ToDo('learn Python', 'make some tasks', 1, False),
            ToDo('learn OOP', "that's hard thing", 2, False)
        ])
    else:
        raise ValueError(f"Unknown repo type: {repo}")


def get_todo_repo(db: Session = Depends(get_db)):
    return get_repo("db", db)
