class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Create three objects
c1 = Car("Toyota", "Corolla")
c2 = Car("Honda", "Civic")
c3 = Car("Ford", "Mustang")

print(c1.brand, c1.model)
print(c2.brand, c2.model)
print(c3.brand, c3.model)
