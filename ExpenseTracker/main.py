import expense
import expense_tracker
import storage
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

def get_int(prompt, min_value=None, max_value=None):

    while True:
        try:
            value = int(input(prompt))

        except ValueError:
            print("Please enter a valid integer")
            continue

        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}")
            continue

        if max_value is not None and value > max_value:
            print(f"Value must be at most {max_value}")
            continue

        return value


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

    option = get_int("------>",0,6)


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
        
        remove = get_int("\nEnter id to remove\n")
        res = tracker.remove_expense(remove)
        print(res)
    
    elif option == 3:
        print(
            "\nselect between these options: \n" +
            "\n0. back to menu\n" +
            "\n1. show all extenses\n" +
            "\n2. show specific category\n"
        )
        
        selection = get_int("------> ",0,2)
        if selection == 0:
            continue
        if selection == 1:
            print(tracker.show_all())
        if selection == 2:
            cat = input("Enter your category:")
            print(tracker.show_category(cat))

    
    elif option == 4:
        print(
            "\nselect between these options: \n" +
            "\n0. back to menu\n" +
            "\n1. show total amount\n" +
            "\n2. show specific category amount\n"
        )
        
        selection = get_int("------> ",0,2)
        if selection == 0:
            continue
        if selection == 1:
            print(tracker.total())
        if selection == 2:
            cat = input("Enter your category:")
            print(tracker.total_category(cat))
        
    elif option == 5:

            count = get_int("Enter the count of highest values you want: ",1,len(tracker.expenses))
            print(tracker.highest_amounts(count))

    elif option == 6:

        print(
            "\nselect between these options: \n" +
            "\n0. back to menu\n" +
            "\n1. save data\n" +
            "\n2. import data\n"
        )
        selection = get_int("------> ",0,2)
        if selection == 0:
            continue
        if selection == 1:
            object_list_data = tracker.expenses
            storage.save_data(object_list_data)
        if selection == 2:
            loaded = storage.load_data("expenses.json")
            for item in loaded:
                tracker.add_expense(item)
                print(
                    f"\n***Object Added***"
                    f"\nId: {item.id}"
                    f"\namount: {item.amount}"
                    f"\ndescription: {item.description[:30]}"
                    f"\ndate: {item.date}\n"
                )