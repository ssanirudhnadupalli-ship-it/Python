from abc import ABC, abstractmethod

class Course(ABC):

    @abstractmethod
    def start(self):
        pass

    def display_course_details(self):
        print("Course: Python Programming")
        print("Duration: 3 Months")


class PythonCourse(Course):

    def start(self):
        print("Python course has started")


obj = PythonCourse()
obj.start()
obj.display_course_details()