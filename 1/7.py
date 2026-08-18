from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def role(self):
        pass

class Student(Person):
    def role(self):
        return "I am a Student."

class Teacher(Person):
    def role(self):
        return "I am a Teacher."

print(Student().role())
print(Teacher().role())
