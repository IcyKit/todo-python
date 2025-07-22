from fastapi import FastAPI
from middleware.logger import log_request
from api.todo import router as todo_router
from db.db import Base, engine
from prometheus_fastapi_instrumentator import Instrumentator

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todo_router)
Instrumentator().instrument(app).expose(app, include_in_schema=False)
app.middleware("http")(log_request)
