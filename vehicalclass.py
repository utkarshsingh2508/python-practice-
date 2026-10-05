class Vehical:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vehical):
    def __init__(self,brand,model,seat):
        super().__init__(brand,model)
        self.seat = seat

class Bike(Vehical):
    def __init__(self, brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc = engine_cc

c1 = Car("suzuki","Dezire",4)
b1 = Bike("Royal enfield","Meteor",250)

print(f"{c1.brand} {c1.model} {c1.seat} Seater")
print(f"{b1.brand} {b1.model} {b1.engine_cc} cc engine")