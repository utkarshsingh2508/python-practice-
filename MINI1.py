class User:
    def __init__(self,name):
        self.name = name

class Message:
    def __init__(self,user,text):
        self.user = user
        self.text = text

class Chatroom:
    def __init__(self,name):
        self.name = name
        self.users = []
        self.messages = []

    def join(self,user):
        self.users.append(user)
        print(user.name,":","Joind the chatroom")

    def leave(self,user):
        self.users.remove(user)
        print(user.name,":","Left the chatroom")

    def send_message(self,user,text):
        if user in self.users:
            self.messages.append(Message(user,text))
            print(user.name,":",text)

    def history(self):
        print("\nMessage history")
        for message in self.messages:
            print(message.user.name,":",message.text)

u1 = User("Golu")
u2 = User("Utkarsh")

chatroom = Chatroom("Python chatroom")

chatroom.join(u1)
chatroom.join(u2)

chatroom.send_message(u1,"Hello")
chatroom.send_message(u2,"Hello Golu")

chatroom.history()

chatroom.leave(u1)