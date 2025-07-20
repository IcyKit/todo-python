from repository.todo.todo_repository import ToDoRepository


class ToDoDBRepository(ToDoRepository):
    def __init__(self, todos):
        self.todos = todos

    def get_all(self):
        pass

    def get_by_id(self, id: str | int):
        pass

    def create(self, todo):
        pass

    def delete_by_id(self, id):
        pass

    def update(self, id):
        pass
