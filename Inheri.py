#creating the Base class
class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("I am a Vehicle")
        print("Mileage is ",self.mileage)
        print("Cost is ",self.cost)
v1= Vehicle(300,1000)
v1.show_details()
class Car(Vehicle):
    def show_car(self):
        print("i am a car")
c1=Car(200,1200)
c1.show_details()
c1.show_car()