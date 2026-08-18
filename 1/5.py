from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} via UPI."

class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} via Card."

print(UPIPayment().pay(500))
print(CardPayment().pay(1000))
