import student
import json


def save_data(students_list):

    with open("students.json" , "w") as std:
            save_list = []
            for student in students_list:
                data = {
                    "id": student.id,
                    "name": student.name,
                    "age": student.age,
                    "grade": student.grade
                    }
                save_list.append(data)
            json.dump(
                save_list,
                std,
                indent = 4
                )
    print("data saved successfully")

def load_data(students_list):
    students_list.clear()
        
    with open("students.json", "r") as std:
        data = json.load(std)

    max_id = 0
    for item in data:
        student_obj = student.Student(
            item["name"],
            item["age"],
            item["grade"],
            item["id"]
        )
        students_list.append(student_obj)
        if item["id"] > max_id:
            max_id = item["id"]
    student.Student.first_id = max_id + 1
    return students_list