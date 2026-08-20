from abc import ABC, abstractmethod

class ECommercePayment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(ECommercePayment):
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class CreditCard(ECommercePayment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


class DebitCard(ECommercePayment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Debit Card")


class NetBanking(ECommercePayment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Net Banking")


UPI().pay(500)
CreditCard().pay(1000)
DebitCard().pay(750)
NetBanking().pay(1500)