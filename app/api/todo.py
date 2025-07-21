from typing import List
from fastapi import APIRouter, Depends, HTTPException
from models.todo import ToDo, ToDoModel
from repository.todo.factory import get_repo, get_todo_repo
from schemas.todo import ToDoCreate, ToDoType, ToDoUpdate

router = APIRouter()


@router.get("/todo", response_model=List[ToDoType])
def get_todos(todo_repository=Depends(get_todo_repo)):
    return todo_repository.get_all()


@router.get("/todo/{todo_id}", response_model=ToDoType)
async def get_todo(todo_id: str, todo_repository=Depends(get_todo_repo)):
    return todo_repository.get_by_id(todo_id)


@router.post('/todo')
async def create_todo(todo: ToDoCreate, todo_repository=Depends(get_todo_repo)):
    return todo_repository.create(todo)


@router.delete('/todo/{todo_id}', response_model=ToDoType)
async def delete_todo(todo_id: str, todo_repository=Depends(get_todo_repo)):
    deleted = todo_repository.delete_by_id(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return deleted


@router.put('/todo/{todo_id}')
async def update_todo(todo: ToDoUpdate, todo_id: str, todo_repository=Depends(get_todo_repo)):
    return todo_repository.update(todo, todo_id)
