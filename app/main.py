from fastapi import FastAPI
from middleware.logger import log_request
from api.todo import router as todo_router
from db.db import Base, engine
from models.todo import ToDoModel

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todo_router)
app.middleware("http")(log_request)


@app.get("/")
def read_root():
    return {"Hello": "World"}
