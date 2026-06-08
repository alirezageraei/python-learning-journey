class ToDoList:
    """
    ToDoList will sort and manage all tasks with their attributes
    """
    def __init__(self):
        self.tasks = []

    def add_task(self,task):

        # add task by its name
        self.tasks.append(task)
    
    def remove_task(self, task_id):

        # remove task by its name
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"Task {task.name} remowed successfully!")
    
    def task_review(self):
        for task in self.tasks:
            print(
                f"task: {task.name}\ndescription: {task.description[:30]}\nPriority: {task.priority}\n\n" + "-" * 20)