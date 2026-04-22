class Vehicle:
    def vehicle_info(self):
        print("inside vehicle class")
class Car(Vehicle):        
    def car_info(self):
        print("inside car class")
c1=Car()
c1.vehicle_info()
c1.car_info()