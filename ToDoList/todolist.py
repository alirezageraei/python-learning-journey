class ToDoList:
    """
    ToDoList will sort and manage all tasks with their attributes
    """
    def __init__(self, task):
        self.tasks = []

    def add_task(self,task):

        # add task by its name
        self.tasks.append(task)
    
    def remove_task(self, task):

        # remove task by its name
        self.tasks.remove(task)
    
    def task_review(self):
        for task in self.tasks:
            return {
                "task": task.name,
                "description": task.description[:30],
                "Priority" : task.priority
            }