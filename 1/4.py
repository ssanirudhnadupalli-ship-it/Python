from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        return "Writing code..."

class Tester(Employee):
    def work(self):
        return "Testing software..."

print(Developer().work())
print(Tester().work())
