from typing import List
from fastapi import FastAPI
from models.todo import ToDo
from schemas.todo import ToDoType
from api.todo import router as todo_router

app = FastAPI()
app.include_router(todo_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}