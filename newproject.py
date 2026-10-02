def registration():

    print("----Quiz registration----")
    create_username = input("Create username for quiz : ")
    create_password = input("Create password for quiz : ")

    if len(create_username) < 4:
        print("Username too short.")
    elif len(create_password) < 6:
        print("Password is weak") 
    else:
        print("Registration successful!")
    return create_username,create_password
 

def login(saved_username,saved_password):
   print("\n----Quiz login----")
   username = input("Enter username : ")
   password = input("Enter password : ")

   if username == saved_username and password == saved_password:
       print("Access granted to quiz.")
       return True
   elif username == saved_username and password != saved_password:
       print("Wrong password")
       return False
   else:
       print("Do registration first.")
       return False



#quiz game
def quiz_game():
  enter_player_name = input("\nEnter your name : ")

  print("\n-----Quiz game-----\n")
  print("Hello",enter_player_name)
  print("You have entered a quiz game. ""\n""To win you have to score 8 points out of 10 points. ")
  print("Total question are 5 each question is of 2 points.")

  print("\n--Let's start game--\n")

  point = 0
  print("1.What is the captial of India?")
  answer1 = "Delhi"
  player_answer_1 = input("Enter your answer : ")
  if player_answer_1.lower() == answer1.lower():
      print("Correct answer!")
      point = point + 2
  else:
     print("Wrong answer!")

  print("2.Which language is mainly used in Ai and machine learning")
  answer2 = "Python"
  player_answer_2 = input("Enter your answer : ")
  if player_answer_2.lower() == answer2.lower():
     print("Correct answer!")
     point = point + 2
  else:
      print("Wrong answer!")

  print("3.How many continent are there in the world?")
  answer3 = "7"
  player_answer_3 = input("Enter your answer : ")
  if player_answer_3.lower() == answer3.lower():
     print("Correct answer!")
     point = point + 2
  else:
     print("Wrong answer!")

  print("4.What does cpu stand for?")
  answer4 = "Central processing unit"
  player_answer_4 = input("Enter your answer : ")
  if player_answer_4.lower() == answer4.lower():
     print("Correct answer!")
     point = point + 2
  else:
     print("Wrong answer!")

  print("5.Which planet is known as the red planet?")
  answer5 = "Mars"
  player_answer_5 = input("Enter your answer : ")
  if player_answer_5.lower() == answer5.lower():
     print("Correct answer!")
     point = point + 2
  else:
      print("Wrong answer!")

  print("Your total point is " ,point)

  if point >= 8:
     print("\n----Congratulation---- \n You just won 7 crore!\n")
  else:
     print("\nBetter luck next time!\n")


saved_username,saved_password = registration()

if login(saved_username,saved_password):
    quiz_game()



       