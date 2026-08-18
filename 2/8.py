class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

p1 = Product("Laptop", 60000, 5)
print("Product:", p1.name, "Price:", p1.price, "Quantity:", p1.quantity)
