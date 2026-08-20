from abc import ABC, abstractmethod

class UniversityCourse(ABC):

    @abstractmethod
    def course_details(self):
        pass


class Engineering(UniversityCourse):
    def course_details(self):
        print("Engineering course - 4 years")


class Medical(UniversityCourse):
    def course_details(self):
        print("Medical course - 5.5 years")


class Management(UniversityCourse):
    def course_details(self):
        print("Management course - 2 years")


Engineering().course_details()
Medical().course_details()
Management().course_details()