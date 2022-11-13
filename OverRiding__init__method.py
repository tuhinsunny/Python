#creating the Base class
class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("I am a Vehicle")
        print("Mileage is ",self.mileage)
        print("Cost is ",self.cost)
class Car(Vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp
    def show_car_details(self):
        print("I am a car")
        print("Number of tyres are ",self.tyres)
        print("The horse power is ",self.hp)
c1=Car(500,50000,8,200)
c1.show_details()
c1.show_car_details()