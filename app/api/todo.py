from typing import List
from fastapi import APIRouter, Depends, HTTPException
from models.todo import ToDo, ToDoModel
from repository.todo.factory import get_repo, get_todo_repo
from schemas.todo import ToDoCreate, ToDoType, ToDoUpdate

router = APIRouter(prefix='/todos', tags=["ToDo"])


@router.get("", summary="Получить все ToDo", response_model=List[ToDoType])
def get_todos(todo_repository=Depends(get_todo_repo)):
    return todo_repository.get_all()


@router.get("/{todo_id}", summary="Получить ToDo по ID", response_model=ToDoType)
async def get_todo(todo_id: str, todo_repository=Depends(get_todo_repo)):
    return todo_repository.get_by_id(todo_id)


@router.post('/todos', summary="Создать новый ToDo")
async def create_todo(todo: ToDoCreate, todo_repository=Depends(get_todo_repo)):
    return todo_repository.create(todo)


@router.delete('/todos/{todo_id}', summary="Удалить ToDo по ID", response_model=ToDoType)
async def delete_todo(todo_id: str, todo_repository=Depends(get_todo_repo)):
    deleted = todo_repository.delete_by_id(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return deleted


@router.put('/todos/{todo_id}', summary="Обновить ToDo по ID")
async def update_todo(todo: ToDoUpdate, todo_id: str, todo_repository=Depends(get_todo_repo)):
    return todo_repository.update(todo, todo_id)
