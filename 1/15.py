from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass

    def display_balance(self):
        print("Balance: ₹50,000")


class SavingsAccount(BankAccount):

    def calculate_interest(self):
        balance = 50000
        interest = balance * 0.05
        print("Interest:", interest)


obj = SavingsAccount()
obj.calculate_interest()
obj.display_balance()