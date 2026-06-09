import expense
import expense_tracker

from  datetime import datetime as dt
from pytz import timezone as zone

def get_info():

    amount = int(input("Amount: "))
    disc = input("discription: ")
    cat = input("category")
    date = dt.now(zone("Asia/Tehran"))
    date = date.date()
    return amount, disc, cat, date

def make_expense_obj():
    (amount, disc, cat, date) = get_info()
    return expense.Expense(amount,disc,cat,date)


tracker = expense_tracker.ExpenseTracker()

while True:

    print("\n***Choose one of these options***\n")
    print("0. Exit")
    print("1. Add extense")
    print("2. Remove extense")
    print("3. Show extense")
    print("4. Show total")
    print("5. Show highest values")
    print("6. Save and Import")

    try:
        option = int(input("----------->"))
        if option not in range(0,7):
            raise ValueError("index out of range")
    except ValueError as e:
        print(e)
        continue

    if option == 0:
        
        print("\n***Thanks for using our app***\n")
        break

    elif option == 1:

        expense_obj = make_expense_obj()
        tracker.add_expense(expense_obj)
        print(
            f"\n***Object Added***"
            f"\nId: {expense_obj.id}"
            f"\namount: {expense_obj.amount}"
            f"\ndescription: {expense_obj.description[:30]}"
            f"\ndate: {expense_obj.date}\n"
        )
    
    elif option == 2:
        
        remove = int(input("\nId to remove: \n"))
        res = tracker.remove_expense(remove)
        print(res)
    
    elif option == 3:
        print(
            "\nselect between these options: \n" +
            "\n1. show all extenses\n" +
            "\n2. show specific category\n"
        )
        try:
            selection = int(input("-------->"))
            if selection not in range(1,3):
                raise ValueError("index out of range")
        except ValueError as e:
            print(e)
            continue

        if selection == 1:
            print(tracker.show_all())
        if selection == 2:
            cat = input("Enter your category:")
            print(tracker.show_category(cat))

    
    elif option == 4:
        print(
            "\nselect between these options: \n" +
            "\n1. show total amount\n" +
            "\n2. show specific category amount\n"
        )
        try:
            selection = int(input("-------->"))
            if selection not in range(1,3):
                raise ValueError("index out of range")
        except ValueError as e:
            print(e)
            continue

        if selection == 1:
            print(tracker.total())
        if selection == 2:
            cat = input("Enter your category:")
            print(tracker.total_category(cat))
        
    elif option == 5:
        try:
            count = int(input("Enter the count of highest values you want: "))
            print(tracker.highest_amounts(count))
        except ValueError:
            print("count must be an Integer")
            continue