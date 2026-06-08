import todolist
import task
import storage


def get_info():
    
    # gets nessesary informations
    name = input("Task name: ")
    describe = input("Task description: ")
    priority = input("Task Priority\nchoose between:\nHigh\nMedium\nLow\n_______:")

    return name, describe, priority

def create_task():
    
    #creates a task
    info = get_info()
    return task.Task(info[0],info[1],info[2])

def add_to_todolist(todolist,task):

    # adds tasks to todolist
    todolist.add_task(task)
    print("*"*30 +"Task successfully added to ToDoList"+ "*"*30)

# --------------------------------------------------------------------- #

todo = todolist.ToDoList()

while True:
    print("-"*20 + "\nChoose between this options\nOr Enter 0 to Exit\n"+"-"*20)
    print("1. Add new task")
    print("2. Remove task")
    print("3. View all tasks")
    print("4. Save tasks")
    print("5. Load tasks\n")

    choose = int(input("(0 - 5): "))
    print("\n"+"*"*30)

    if choose == 0:
        break

    elif choose == 1:

        while True:

            task_obj = create_task()
            add_to_todolist(todo, task_obj)
            repeat = input("For add another task, Enter '+'\nand for return to menu press Enter: ")
            if repeat != '+':
                break

    elif choose == 2:

        while True:

            try:
                obj_to_remove = int(input("enter the id for remove: "))
            except ValueError as e:
                print(f"id must be an Integer!")
                continue

            todo.remove_task(obj_to_remove)

            repeat = input("For add another task, Enter '+'\nand for return to menu press Enter")
            if repeat != '+':
                break
    elif choose == 3:
        
        tasks = todo.task_review()
        print(tasks)

    elif choose == 4:

        data = []
        for task in todo.tasks:
            item = {
                "id": task.id,
                "name": task.name,
                "discription": task.description,
                "priority": task.priority
            }
            data.append(item)

        storage.save_data(data)

    elif choose == 5:

        file_name = input("\nEnter file name or path: \n")
        loaded_list = storage.load_data(file_name)
        for task in loaded_list:
            todo.add_task(task)



        """for desc in task.description:
        res = ''
        for char in desc:
            if char != ",":
                res += char
            else:
                res += " " """
            