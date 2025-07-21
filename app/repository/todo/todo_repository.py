from abc import ABC, abstractmethod


class ToDoRepository(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_by_id(self, id: int): ...
    @abstractmethod
    def get_all(self): ...
    @abstractmethod
    def delete_by_id(self, id: int): ...
    @abstractmethod
    def create(self, todo): ...
    @abstractmethod
    def update(self, todo, id): ...
