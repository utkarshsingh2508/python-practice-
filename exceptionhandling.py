try:
    with open("data.txt","r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("End of code!")
