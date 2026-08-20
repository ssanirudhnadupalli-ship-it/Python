from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_company(self):
        print("Company: HIE Tech Solutions")


class Developer(Employee):

    def calculate_salary(self):
        print("Salary: ₹50,000")


obj = Developer()
obj.calculate_salary()
obj.display_company()