class Person:
    def __init__(self,name,age=None,address=None):
        self.name = name
        self.age = age
        self.address = address

i = Person("Utkarsh")
j = Person("Golu",21)
k = Person("Bantu",25,189)
print(f"{i.name},\n{j.name},{j.age},\n{k.name},{k.age},{k.address}")

