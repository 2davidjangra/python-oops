class Vehicle:

    def start(self):
        print("Vehicle Starts")

class Car(Vehicle):

    def start(self):
        print("Car Starts With Key")

class Bike(Vehicle):

    def start(self):
        print("Bike Starts With Self-Start")


vehicles = [Car(), Bike()]

for v in vehicles:
    v.start()
