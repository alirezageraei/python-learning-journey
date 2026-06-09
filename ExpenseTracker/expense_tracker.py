class ExpenseTracker:

    def __init__(self):
        
        self.expenses = []

    def add_expense(self, expense_obj):
        self.expenses.append(expense_obj)
    
    def remove_expense(self, id_to_remove):

        for obj in self.expenses:
            if obj.id == id_to_remove:
                self.expenses.remove(obj)
                return("\n***Object removed successfully***\n")
        return f"\nNo object found with Id {id_to_remove}\n"
    
    
    def show_all(self):

        if not self.expenses:
            return "\n***Track list in empty***\n"
        else:
            res = "" 
            for obj in self.expenses:
                res += (
                    f"\nID: {obj.id}"+
                    f"\namount: {obj.amount}"+
                    f"\ndescription: {obj.description}"+
                    f"\ncategory: {obj.category}\n"+
                    "-" * 30 
                )
            
            return res

    def show_category(self, cat_to_show):
        
        found = False
        res = ""
        for obj in self.expenses:
            if obj.category == cat_to_show:
                found = True
                res += (
                    f"\nID: {obj.id}"+
                    f"\namount: {obj.amount}"+
                    f"\ndescription: {obj.description}"+
                    f"\ncategory: {obj.category}\n"+
                    "-" * 30 
                )
        if not found:
            return "\n***This category is not exist***\n"
        return res

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
        sorted_items = sorted(
            self.expenses,
            key=lambda obj: obj.amount,
            reverse=True
        )

        top_x = sorted_items[:x]

        res = "\n***These are the Highest amount of your expenses***\n"

        for obj in top_x:
            res += (
                f"\nId: {obj.id}"
                f"\namount: {obj.amount}"
                f"\ncategory: {obj.category}"
                "\n" + "-" * 20
            )

        return res