class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

l1 = Laptop("Dell", "16GB", "i7", 85000)
print("Brand:", l1.brand, "RAM:", l1.ram, "Processor:", l1.processor, "Price:", l1.price)
