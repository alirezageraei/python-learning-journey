class ExpenseTracker:

    def __init__(self):
        
        self.expenses = []

    def add_expense(self, expense_obj):
        
        self.expenses.append(expense_obj)
        return "\n***Expense added to tracker***\n"
    
    def delete_expense(self, obj_id):

        for obj in self.expenses:
            if obj.id == obj_id:
                self.expenses.remove(obj)
                return f"\n***Object with id {obj_id} deleted***\n"
        
        return f"\n***This id is not valid***\n"
    
    
    def show_all(self):

        if not len(self.expenses):
            return "\n***Track list in empty***\n"
        else:
            res = ""
            for obj in self.expenses:
                res += (
                    "-" * 30 +
                    f"\nID: {obj.id}"
                    f"\namount: {obj.amount}"
                    f"\ndescription: {obj.description}"
                    f"\ncategory: {obj.category}\n"
                    "-" * 30 
                )
            
            return res

    def show_category(self, cat_to_show):
        
        found = False
        for obj in self.expenses:
            if obj.category == cat_to_show:
                found = True
                print(
                    "-" * 30 +
                    f"\nID: {obj.id}"
                    f"\namount: {obj.amount}"
                    f"\ndescription: {obj.description}"
                    f"\ncategory: {obj.category}"
                    "-" * 30 
                )
        if not found:
            return "\n***This category is not exist***\n"

    def total(self):

        total = 0
        for obj in self.expenses:
            total += obj.amount
        
        return f"\n***Total amount is {total}***\n"
    
    def total_category(self, cat_to_sum):
        
        total = 0
        cat_exist = False
        for obj in self.expenses:
            if obj.category == cat_to_sum:
                total += obj.amount
                cat_exist = True
        if cat_exist:
            return f"\n***Total amount of {cat_to_sum} expense is {total}***\n"
        else:
            return "\n***This category is not exist***\n"
        
    def highest_amounts(self, x):
        """
        returns the x highest values
        """
        top_x = []
        items = []

        for obj in self.expenses:
            addition = (obj.id, obj.amount)
            items.append(addition)

        while len(top_x) < int(x):
            top_x.append(max(items))
            items.remove(max(items))
        
        return (
            f"\n***These are the Highest amount of your expenses***\n"+
            f"Id: {top_x[0][0]}\namount: {top_x[0][1]}\n" +
            f"Id: {top_x[1][0]}\namount: {top_x[1][1]}\n" +
            f"Id: {top_x[2][0]}\namount: {top_x[2][1]}\n"
            )

        