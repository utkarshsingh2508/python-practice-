while True:
    user_input = input("enter your number:")

    if(user_input=="quit"):
       break
    n = int(user_input)
    
    if (n>0):
        print("positive")
    elif(n<0):
        print("negative")
    else:
        print("zero")
    




