from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

class Defender(Car):
    def mileage(self):
        print("The mileage is 5kmpl.")
class Tesla(Car):
    def mileage(self):
        print("The mileage is 7kmpl.")
d=Defender()
d.mileage()
i=Tesla()
i.mileage()