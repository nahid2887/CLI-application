import os
import json
from employee import Employee

employees = []




def load_employees():
    if os.path.exists("employees.json"):
        with open("employees.json", "r") as file:
            data = json.load(file)
            for item in data:
                employees.append(
                    Employee(
                        emp_id=item['emp_id'],
                        name=item['name'],
                        designation=item['designation'],
                        number=item.get('number', 'N/A'),
                        salary=item.get('salary', 0.0)  # Default salary to 0.0 if missing
                    )
                )
        print("Employee data loaded successfully from JSON!")
    else:
        print("No JSON file found. Starting with an empty employee list.")


def save_employees():
    with open("employees.json", "w") as file:
        data = [emp.__dict__ for emp in employees]
        json.dump(data, file, indent=4)
    print("Employee data saved successfully to JSON!")


def save_employees_to_txt():
    with open("employees.txt", "w") as file:
        for emp in employees:
            # Include salary in the saved text
            file.write(f"{emp.emp_id},{emp.name},{emp.designation},{emp.number},{emp.salary}\n")
    print("Employee data saved successfully to TXT!")



def add_employee():
    emp_id = input("Enter Employee ID: ").strip()
    # Check the employee ID already exists
    if any(emp.emp_id == emp_id for emp in employees):
        print(f"Employee with ID {emp_id} already exists!")
        return
    name = input("Enter Employee Name: ").strip()
    designation = input("Enter Employee Designation: ").strip()
    number = input("Enter Employee Phone: ").strip()

    while True:
        try:
            salary = float(input("Enter Employee Salary: ").strip())
            if salary < 0:
                print("Salary cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the salary.")

    employees.append(Employee(emp_id, name, designation, number, salary))
    save_employees()
    save_employees_to_txt()

    print("Employee added successfully!")


def update_employee():
    emp_id = input("Enter Employee ID to Update: ").strip()
    for emp in employees:
        if emp.emp_id == emp_id:
            emp.name = input(f"Enter New Employee Name (current: {emp.name}): ").strip() or emp.name
            emp.designation = input(f"Enter New Employee Designation (current: {emp.designation}): ").strip() or emp.designation
            emp.number = input(f"Enter New Employee Phone (current: {emp.number}): ").strip() or emp.number
            emp.salary = input(f"Enter New Employee Salary (current: {emp.salary}): ").strip()
            save_employees()
            save_employees_to_txt()
            print("Employee information updated successfully!")
            return

    print("Employee not found!")


def delete_employee(emp_id):
    global employees
    for i, emp in enumerate(employees):
        if emp.emp_id == emp_id:
            del employees[i]
            save_employees()
            save_employees_to_txt()
            return
    raise ValueError(f"Employee with ID {emp_id} not found.")


def view_employees():
    if not employees:
        print("No employees found.")
    for emp in employees:
        print(emp)

def search_employee():
    keyword = input("Enter Employee Name, Designation, Phone, or Salary to Search: ").strip().lower()
    results = [
        emp for emp in employees
        if keyword in emp.name.lower()
        or keyword in emp.designation.lower()

    ]
    if not results:
        print("No employees found.")
    else:
        print("\nMatching Employees:")
        for emp in results:
            print(emp)

