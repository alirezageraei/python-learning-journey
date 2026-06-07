class Task:
    """
    Task object has name, description and priority.
    each task will be placed in ToDoList as its priority.
    """
    def __init__(self, name, descriotion, priority):
        self.name = name
        self.description = descriotion
        self.priority = priority


