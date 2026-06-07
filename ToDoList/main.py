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


"""    for desc in task.description:
        res = ''
        for char in desc:
            if char != ",":
                res += char
            else:
                res += " " """
            