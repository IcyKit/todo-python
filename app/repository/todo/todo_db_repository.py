from schemas.todo import ToDoCreate, ToDoUpdate
from models.todo import ToDoModel
from sqlalchemy.orm import Session
from repository.todo.todo_repository import ToDoRepository


class ToDoDBRepository(ToDoRepository):
    def __init__(self, db: Session):
        self.todos = []
        self.db = db

    def get_all(self):
        todos = self.db.query(ToDoModel).all()
        return todos

    def get_by_id(self, id: str | int):
        todo = self.db.query(ToDoModel).filter(ToDoModel.id == int(id)).first()
        if not todo:
            return None
        return todo

    def create(self, todo: ToDoCreate):
        todo_model = ToDoModel(**todo.model_dump())
        self.db.add(todo_model)
        self.db.commit()
        self.db.refresh(todo_model)
        return todo_model

    def delete_by_id(self, id: str):
        todo = self.db.query(ToDoModel).filter(ToDoModel.id == int(id)).first()
        print(todo)
        if not todo:
            return None
        self.db.delete(todo)
        self.db.commit()
        return todo

    def update(self, todo_data: ToDoUpdate, id: str):
        todo = self.db.query(ToDoModel).filter(ToDoModel.id == int(id)).first()
        if not todo:
            return None

        for key, value in todo_data.model_dump(exclude_unset=True).items():
            setattr(todo, key, value)

        self.db.commit()
        self.db.refresh(todo)
        return todo
