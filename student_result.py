name = input("Enter student name: ")

marks = []

subjects = ["English", "Maths", "Physics", "Chemistry", "Computer"]

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks for {subject}: "))

            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100.")
                continue

            marks.append(mark)
            break

        except ValueError:
            print("Please enter a valid number.")

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

if any(mark < 40 for mark in marks):
    result = "FAIL"
else:
    result = "PASS"

print("\n----- Student Result -----")
print("Name:", name)
print("Total:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)