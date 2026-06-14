class Expense:

    expense_id = 1
    def __init__(self, amount, description, category, date, obj_id=None):
        
        if obj_id == None:
            self.id = Expense.expense_id
            Expense.expense_id += 1
        else:
            self.id = obj_id        
    
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date