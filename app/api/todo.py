from typing import List
from fastapi import APIRouter

from repository.todo.factory import get_repo
from schemas.todo import ToDoType

router = APIRouter()

todo_repository = get_repo("memory")


@router.get("/todo", response_model=List[ToDoType])
def get_todos():
    return todo_repository.get_all()


@router.get("/todo/{todo_id}", response_model=ToDoType)
async def get_todo(todo_id):
    return todo_repository.get_by_id(todo_id)


@router.post('/todo')
async def create_todo(todo: ToDoType):
    return todo_repository.create(todo)


@router.delete('/todo/{todo_id}', response_model=ToDoType)
async def delete_todo(todo_id):
    return todo_repository.delete_by_id(todo_id)


@router.put('/todo')
async def update_todo(todo: ToDoType):
    return todo_repository.update(todo)
