student = {
    "Golu" : 85,
    "Ravina" : 95,
    "Sourabh" : 80,
    "Bantu" : 90
}
while True:
    key = input(f" A - to add student \n B - to update marks \n C - search for student \n D - display data \n Q - Quit \n Enter key: ").upper()
    if key == "A":
        student_name = input("Enter student name:")
        student_marks = int(input("Enter student marks:"))
        new_student = {student_name : student_marks}
        student.update(new_student)
        print(student)
    elif key == "B":
        name = input("Enter a student name:")
        if name in student:
            marks = int(input("Enter new marks:"))
            student[name] = marks
            print("Marks updated successfully!")
        else:
            print("student not found!")
        print(student)
    elif key == "C":
        name = input("Enter a student name:")
        if name in student:
            print(f"{name} marks are : {student.get(name)}")
        else:
            print("student not found!")
    elif key == "D":
        for i, j in student.items():
            print(f"{i} : {j}")
    elif key == "Q":
        break
    else:
        print("invalid input")

        

