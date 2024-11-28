class Employee:
    def __init__(self, emp_id, name, designation, number, salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.number = number
        self.salary = salary
        #self.email = email



    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Designation: {self.designation}, Phone: {self.number},  Salary: {self.salary}"



