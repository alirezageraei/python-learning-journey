import json
import expense

def save_data(object_list):

    data = []
    for obj in object_list:
        data.append({
        "id" : obj.id,
        "amount" : obj.amount,
        "description" : obj.description,
        "category" : obj.category,
        "date" : obj.date
    })
    with open("expenses.json", "w") as exp:
            json.dump(data, exp, indent=4)
            print(f"\n***Data saved in expenses.json successfully***\n")

def load_data(filename):

    
    with open(filename, "r") as f:
        data = json.load(f)
        max_id = 0
        obj_list = []
        for item in data:
            expense_obj = expense.Expense(
                item["amount"],
                item["description"],
                item["category"] ,
                item["date"],
                item["id"]
            )
            obj_list.append(expense_obj)
            if expense_obj.id > max_id:
                max_id = expense_obj.id
        expense.Expense.expense_id = max_id + 1
    print(f"\n***Data imported from {filename} successfully***\n")
    return obj_list
