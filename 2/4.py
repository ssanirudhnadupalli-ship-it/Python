class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

m1 = Mobile("Samsung", "Galaxy S21", 70000)
print("Brand:", m1.brand, "Model:", m1.model, "Price:", m1.price)
