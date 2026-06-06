import student

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
    print(f"{student_obj.name} is Added to students list\n" + "-"*30)


# ---------------------------------------------------------------- #


std_list = []

choose = 6
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save Data")
    print("6. Exit")

    option = int(input("Choose an Option(just the number): "))
    # if option.upper() in ["6","EXIT","6. EXIT","6.EXIT"]:
    if option == 6:
        break
    elif option == 1:
        student_info = get_info()
        student_obj = create_student(student_info[0],student_info[1],student_info[2])
        add_student(student_obj, std_list)
    else:
        # raise TypeError("Entered Value must be an Integer")
        break # فعلا این باشه تا آخرسر
