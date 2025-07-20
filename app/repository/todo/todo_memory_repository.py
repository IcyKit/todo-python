from repository.todo.todo_repository import ToDoRepository


class ToDoMemoryRepository(ToDoRepository):
    def __init__(self, todos):
        self.todos = todos

    def get_all(self):
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

    def update(self, todo):
        for i, td in enumerate(self.todos):
            if td.id == int(todo.id):
                self.todos[i] = todo
                return todo
