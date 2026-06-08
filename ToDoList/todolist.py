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

        priority_map = {
            "High": 3,
            "Medium": 2,
            "Low": 1
        }

        sorted_tasks = sorted(
            self.tasks,
            key=lambda task: priority_map.get(task.priority, 0),
            reverse=True
        )

        res = ''

        for task in sorted_tasks:
            res += (
                f"\nid: {task.id}"
                f"\ntask: {task.name}"
                f"\ndescription: {task.description[:30]}"
                f"\nPriority: {task.priority}\n\n"
                + "-" * 20
            )

        return res if res != '' else "\n***Task not found***\n"