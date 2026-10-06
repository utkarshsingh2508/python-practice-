class Player:
    Player_count = 0

    def __init__(self,name,level):
        self.name = name
        self.level = level
        Player.Player_count += 1

p1 = Player("Arpit",25)
p1 = Player("Rohan",38)
P3 = Player("Aman",20)
p4 = Player("Sumit",48)

print(Player.Player_count)