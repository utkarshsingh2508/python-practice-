create_username = input("Create username : ")
create_password = input("Create password : ")


def login_system():
    correct_username = create_username
    correct_password = create_password

    username = input("Enter username : ")
    password = input("Enter password : ")

    if username == correct_username and password == correct_password:
        print("Access granted ")
    elif username == correct_username and password != correct_password:
        print("You have entered wrong password! \nTry again")
    else:
        print("User doesn't exist \nCreate your account first  ")


if len(create_password) <=6:
    print("weak password ")
else:
      login_system()