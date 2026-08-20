from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def calculate_discount(self):
        pass

    def display_product(self):
        print("Product: Laptop")
        print("Price: ₹50,000")


class Laptop(Product):

    def calculate_discount(self):
        price = 50000
        discount = price * 0.10
        print("Discount:", discount)


obj = Laptop()
obj.calculate_discount()
obj.display_product()