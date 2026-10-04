while True:
    n = input("Enter an number : ")
    if n == "quit":
        break
    n = int(n)
    if n >= 0:
        print("Positive")
    elif n < 0:
        print("Negative")
