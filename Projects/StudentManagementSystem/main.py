import student
import storage
# -------------------------------------------------------- #
def get_info():

    while True:
        try:
            name = input("Name: ")
            age = int(input("Age: "))
            grade = float(input("Grade: "))
            return name, age, grade

        except ValueError:
            print("Invalid Input")

def create_student(name, age, grade):

    """ makes the Student object """    
   
    # Validation section
    if not isinstance(name, str):
        raise TypeError("Name should be a string")    
    if not isinstance(age, int):
        raise TypeError("Age should be an integer")
    if not isinstance(grade, float):
        raise TypeError("Grade should be a float")
    if not 0 <= grade <= 100:
        raise ValueError("Grade should be between 0 - 100")
    
    # making object
    return student.Student(name, age, grade)

def add_student(student_obj, append_to):

    # adding student object to the list
    append_to.append(student_obj)
    print(30*"-" + f"\n{student_obj.name} is Added to students list\n" + "-"*30)


# ---------------------------------------------------------------- #


std_list = []

choose = 6
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save Data")
    print("6. Load data")
    print("7. Exit")

    try:
        option = int(input("Choose an Option between 1 - 7\n(just the number): "))
    
    except ValueError:
        print("Invalid Input")
        continue
    
    # if option.upper() in ["6","EXIT","6. EXIT","6.EXIT"]:
    if option == 7:
        break

    elif option == 1:
        while True:
            student_info = get_info()
            student_obj = create_student(student_info[0],student_info[1],student_info[2])
            add_student(student_obj, std_list)
            repeat = input("Enter '+' to do another adding\nor press Enter for main menu ")
            if repeat != "+":
                break

    elif option == 2:
        while True:
            for student in std_list:
                # print(f"name: {student.name}\nage: {student.age}\ngrade: {student.grade}\n" + "***" * 10)
                print(student)
            repeat = input("Enter '+' to see informations again\nor press Enter for main menu ")
            if repeat != "+":
                    break
            
    elif option == 3:

        while True:
            searched_name = input("Enter the name:_________")
            
            for student in std_list:
                if student.name == searched_name:
                    print("-"*20)
                    print(student)
                    break
            repeat = input("Enter '+' to search again\nor press Enter for main menu ")
            if repeat != "+":
                    break

    elif option == 4:
        while True:
            found = False
            Id = int(input("Enter the id you want to remove: "))
            for student in std_list:
                if Id == student.id:
                    std_list.remove(student)
                    print(f"name {student.name} is removed\n---------------------")
                    found = True
                    break
            if not found:
                print("this Id is not exist\n------------------------")
            repeat = input("Enter '+' to delete another item\nor press Enter for main menu ")
            if repeat != "+":
                    break
            
    elif option == 5:
        # save data using storage module
        storage.save_data(std_list)

    elif option == 6:

        try:
            # load data using storage module and put it into std_list
            std_list = storage.load_data(std_list)
        except FileNotFoundError as e:
            print("File not founded")
            continue
    
    else:
        raise TypeError("Entered Value must be an Integer")