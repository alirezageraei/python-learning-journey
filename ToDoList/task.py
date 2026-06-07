class Task:
    """
    Task object has name, description and priority.
    each task will be placed in ToDoList as its priority.
    """
    task_id = 1

    def __init__(self, name, descriotion, priority, task_id=None):
        if task_id is None:
            self.id = Task.task_id
            Task.task_id += 1
        else:
            self.id = task_id

        self.name = name
        self.description = descriotion
        self.priority = priority

        print("-"*30 + "\nTask created: ")
        print(f"name : {self.name}\ndescription: {self.description[:30]}\npriority: {self.priority}")

