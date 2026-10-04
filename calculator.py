def calculator(a,b,operation):
    if (operation == "+"):
        return a+b
    elif (operation == "-"):
        return a-b
    elif(operation == "*"):
        return a*b
    elif(operation == "/"):
        if b != 0 :
            return a/b
        else:
            "Error"

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
operation = str(input("Enter operation : "))

print(calculator(a,b,operation))




