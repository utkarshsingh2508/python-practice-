#quiz game

enter_player_name = input("Enter your name : ")

print("\n-----quiz game-----")
print("\nYou have entered quiz game",enter_player_name)
print("You will be asked five question","\nIf you score 8/10 you will we rewarded"," \nEach question is of 2 points")
 
print("\nLET'S START")
print("\nFirst question : ")

total_point = 0
print("1. What is the capital of India?")
answer1 = "Delhi"
player_answer1 = input("Enter your answer : ")
if player_answer1.lower() == answer1.lower():
    print("Correct answer ")
    total_point = total_point + 2
else:
    print("Wrong answer")

print("2. Which language is mainly used for AI and Machine Learning?")
answer2 = "Python"
player_answer2 = input("Enter your answer : ")
if player_answer2.lower() == answer2.lower():
    print("Correct answer ")
    total_point = total_point + 2
else:
    print("Wrong answer")

print("3. How many continents are there in the world?")
answer3 = "7"
player_answer3 = input("Enter your answer : ")
if player_answer3.lower() == answer3.lower():
    print("Correct answer ")
    total_point = total_point + 2
else:
    print("Wrong answer")

print("4. What does CPU stand for?")
answer4 = "Central Processing Unit"
player_answer4 = input("Enter your answer : ")
if player_answer4.lower() == answer4.lower():
    print("Correct answer ")
    total_point = total_point + 2
else:
    print("Wrong answer")

print("5. Which planet is known as the Red Planet?")
answer5 = "Mars"
player_answer5 = input("Enter your answer : ")
if player_answer5.lower() == answer5.lower():
    print("Correct answer ")
    total_point = total_point + 2
else:
    print("Wrong answer")

print("Your total score is",total_point)
if total_point >=8:
    print("Congratulation you have won 7 crore")