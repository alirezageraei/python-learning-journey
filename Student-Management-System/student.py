class Student:
    """
    
    """

    first_id = 1
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
        self.id = Student.first_id
        Student.first_id += 1

    def __str__(self):
        return (
            f"name: {self.name}\n"
            f"age: {self.age}\n"
            f"grade: {self.grade}\n"
            "-------------------------------"
            )