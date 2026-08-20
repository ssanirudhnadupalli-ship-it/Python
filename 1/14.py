from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def display_shape(self):
        print("Shape: Circle")


class Circle(Shape):

    def area(self):
        radius = 5
        print("Area:", 3.14 * radius * radius)


obj = Circle()
obj.area()
obj.display_shape()