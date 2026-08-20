from abc import ABC, abstractmethod

class ATM(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class Bank(ATM):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful:", amount)
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful:", amount)

    def check_balance(self):
        print("Current Balance:", self.balance)


b = Bank(10000)
b.check_balance()
b.deposit(2000)
b.withdraw(3000)
b.check_balance()