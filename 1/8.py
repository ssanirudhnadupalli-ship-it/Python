from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self, balance):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.04  # 4% interest

class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.01  # 1% interest

print(SavingsAccount().calculate_interest(10000))
print(CurrentAccount().calculate_interest(10000))
