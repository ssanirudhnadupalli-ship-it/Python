class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

# Create one object
e1 = Employee("John", 101)
print("Employee:", e1.name, "| ID:", e1.emp_id)
