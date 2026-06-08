import csv
import task


def save_data(data):

       
    with open("tasks.csv", "w",newline="",encoding="utf-8") as t:
        
        Headings = ["id","name", "discription", "priority"]
        writer = csv.DictWriter(t, fieldnames=Headings)
        writer.writeheader()
        for item in data:
            writer.writerow(item)
    print("\n*****file saved successfully!*****\n")


def load_data(file_name):

    while True:
        # Loads data Line by line from a CSV file
        try:    
            with open(file_name, "r", newline='') as t:
                reader = csv.DictReader(t)
                res = []
                for row in reader:
                    task_obj = task.Task(row["name"],row["discription"],row["priority"],int(row["id"]))
                    res.append(task_obj)
            print("\n*****data imported successfully!*****\n")
            break 
        except FileNotFoundError:
            print(f"Please enter a valid file path, {file_name} not found")
            continue
    max_id = 0
    for i in res:
        if i.id > max_id:
            max_id = i.id
    task.Task.task_id = max_id + 1
    return res 