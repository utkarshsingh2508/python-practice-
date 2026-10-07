with open("log.txt","a") as f:
    f.write("\n Program run successfully")

with open("log.txt","r") as f:
    data = f.read()
    print(data)
