from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def fuel_type(self):
        pass

class PetrolCar(Vehicle):
    def fuel_type(self):
        print("Petrol")

class ElectricCar(Vehicle):
    def fuel_type(self):
        print("Electric")

car1 = PetrolCar()
car2 = ElectricCar()

car1.fuel_type()
car2.fuel_type()