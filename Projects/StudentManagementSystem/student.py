class Student:
    """
    
    """

    first_id = 1
    def __init__(self, name, age, grade, student_id=None):
        self.name = name
        self.age = age
        self.grade = grade
        
        if student_id is None:
            self.id = Student.first_id
            Student.first_id += 1
        else:
            self.id = student_id

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"name: {self.name}\n"
            f"age: {self.age}\n"
            f"grade: {self.grade}\n"
            "-------------------------------"
            )