class Herbivore:
    def eat_plant(self):
        print("Eat only plants")

class Carnivore:
    def eat_meat(self):
        print("Eat only meat")

class Omnivore:
    def eat_both(self):
        print("Eat both plants and meat")

class Bear(Herbivore,Carnivore,Omnivore):
    pass

B1 = Bear()
B1.eat_plant()
B1.Eat_meat()
B1.eat_both()