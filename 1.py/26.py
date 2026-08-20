from abc import ABC, abstractmethod

class Transport(ABC):

    @abstractmethod
    def travel(self):
        pass


class Bus(Transport):
    def travel(self):
        print("Traveling by Bus")


class Train(Transport):
    def travel(self):
        print("Traveling by Train")


class Flight(Transport):
    def travel(self):
        print("Traveling by Flight")


class Cab(Transport):
    def travel(self):
        print("Traveling by Cab")


Bus().travel()
Train().travel()
Flight().travel()
Cab().travel()