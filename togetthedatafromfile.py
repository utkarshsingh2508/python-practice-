with open("names.txt","w") as f:
    for i in range(1,6):
        data = input("Enter names: ")
        f.write(data + "\n")

with open("names.txt","r") as f:
    data1 = f.read()
    print(data1)

