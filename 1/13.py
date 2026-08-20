from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def display_info(self):
        print("Vehicle: Car")


class Car(Vehicle):

    def start(self):
        print("Car starts with a key")


obj = Car()
obj.start()
obj.display_info()