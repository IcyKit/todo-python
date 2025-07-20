class ToDo:
    def __init__(self, title: str, description: str, id: int, is_completed: bool = False,):
        self.title = title
        self.description = description
        self.is_completed = is_completed
        self.id = id
