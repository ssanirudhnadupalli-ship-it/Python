class College:
    def __init__(self, name, location, course):
        self.name = name
        self.location = location
        self.course = course

c1 = College("ABC College", "Hyderabad", "CSE")
c2 = College("XYZ College", "Delhi", "ECE")
c3 = College("LMN College", "Mumbai", "IT")

print(c1.name, "-", c1.location, "-", c1.course)
print(c2.name, "-", c2.location, "-", c2.course)
print(c3.name, "-", c3.location, "-", c3.course)
