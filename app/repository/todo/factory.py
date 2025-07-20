from typing import Literal
from models.todo import ToDo
from repository.todo.todo_db_repository import ToDoDBRepository
from repository.todo.todo_memory_repository import ToDoMemoryRepository


def get_repo(repo: Literal["db", "memory"]):
    if repo == "db":
        return ToDoDBRepository([])
    elif repo == "memory":
        return ToDoMemoryRepository([
            ToDo('learn Python', 'make some tasks', 1, False),
            ToDo('learn OOP', "that's hard thing", 2, False)
        ])
    else:
        raise ValueError(f"Unknown repo type: {repo}")
