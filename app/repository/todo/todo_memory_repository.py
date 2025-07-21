from typing import List
from models.todo import ToDo
from repository.todo.todo_repository import ToDoRepository


class ToDoMemoryRepository(ToDoRepository):
    def __init__(self, todos: List[ToDo]):
        self.todos = todos

    def get_all(self) -> List[ToDo]:
        return self.todos

    def get_by_id(self, id: str | int):
        for todo in self.todos:
            if todo.id == int(id):
                return todo

    def create(self, todo):
        self.todos.append(todo)
        return todo

    def delete_by_id(self, id):
        for todo in self.todos:
            if todo.id == int(id):
                self.todos.remove(todo)
                return todo

    def update(self, todo, id):
        for td in self.todos:
            if td.id == int(id):
                new_td = td.update(todo)
                print(new_td)
                return new_td
