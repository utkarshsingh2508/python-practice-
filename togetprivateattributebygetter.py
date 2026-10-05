class Student:
    def __init__(self,name,roll_no,marks):
        if name != "":
            self.__name = name
        else:
             print("name cannot be empty")
        if roll_no > 0 and roll_no <= 100:
            self.__roll_no = roll_no
        else:
             print("roll number has to be between 1 & 100")

        if marks >= 0:
            self.__marks = marks
        else:
            print(" marks cannot be negative")

    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks

    def set_roll_no(self, new_roll_no):
            if new_roll_no > 0 and new_roll_no <= 100:
                self.__roll_no = new_roll_no

    def set_name(self, new_name):
            if new_name != "":
                self.__name = new_name


s1 = Student("Golu",55,98)
s2 = Student("Bantu",48,80)
s3 = Student("Ram",21,100)

s1.set_marks(95)

print(s1.get_name(),s1.get_roll_no(),s1.get_marks())