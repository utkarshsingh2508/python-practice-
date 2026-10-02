def calculate_result():
    student_name = input("Enter your name : ")

    english = int(input("Enter your English marks : "))
    maths = int(input("Enter your Maths marks : "))
    hindi = int(input("Enter your Hindi marks : "))

    Calculate_total = english+maths+hindi
    total_percent = (Calculate_total/300)*100


    print("\n-----RESULT-----")
    print("Student name = " , student_name)
    print("Total number = ", Calculate_total)
    print("percentage = ", total_percent)

    if total_percent < 33:
        print("You have failed the exams ")
        print("Your grade is F ")
    elif 33 <= total_percent <= 60:
        print("Below average ")
        print("Your grade is C ")
    elif 60 < total_percent <= 75:
        print("Average")
        print("Your grade is B ")
    else:
        print("Good")
        print("Your grade is A ")


calculate_result()



