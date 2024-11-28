from flask import Flask, render_template, request, redirect, url_for
from operations import load_employees, add_employee, update_employee, delete_employee, view_employees, search_employee, \
    employees, save_employees_to_txt, save_employees
from employee import Employee

app = Flask(__name__)

load_employees()



@app.route('/')
def index():
    return render_template('index.html', employees=employees)


@app.route('/add', methods=['GET', 'POST'])
def add_employee_route():
    if request.method == 'POST':
        emp_id = request.form['emp_id'].strip()

        # Check if employee ID already exists
        if any(emp.emp_id == emp_id for emp in employees):
            return render_template(
                'add_employee.html',
                error=f"Employee with ID {emp_id} already exists!"
            )
        name = request.form['name'].strip()
        designation = request.form['designation'].strip()
        number = request.form['number'].strip()
        try:
            salary = float(request.form['salary'].strip())
            if salary < 0:
                return render_template(
                    'add_employee.html',
                    error="Salary cannot be negative."
                )
        except ValueError:
            return render_template(
                'add_employee.html',
                error="Invalid salary. Please enter a numeric value."
            )
        employees.append(Employee(emp_id, name, designation, number, salary))
        save_employees()
        save_employees_to_txt()
        return redirect(url_for('index'))
    return render_template('add_employee.html')


@app.route('/update/<emp_id>', methods=['GET', 'POST'])
def update_employee_route(emp_id):
    emp = next((e for e in employees if e.emp_id == emp_id), None)

    if request.method == 'POST':
        if emp:
            emp.name = request.form['name']
            emp.designation = request.form['designation']
            emp.number = request.form['number']
            emp.salary = request.form['salary']
            save_employees()
            save_employees_to_txt()

            return redirect(url_for('index'))

    return render_template('update_employee.html', employee=emp)


@app.route('/delete/<emp_id>')
def delete_employee_route(emp_id):
    delete_employee(emp_id)
    return redirect(url_for('index'))

@app.route('/search', methods=['GET', 'POST'])
def search_employee_route():
    if request.method == 'POST':
        keyword = request.form['keyword'].lower()
        results = [
            e for e in employees
            if keyword in e.name.lower() or
               keyword in e.designation.lower() # Added salary in the search criteria
        ]
        return render_template('index.html', employees=results)

    # For GET request, just show the homepage
    return render_template('index.html', employees=employees)


@app.route('/view_all')
def view_all_employees_route():
    return render_template('view_all_employees.html', employees=employees)

@app.route('/save_all')
def save_all_route():
    save_employees_to_txt()  # Save employees to the text file
    return redirect(url_for('index'))  # Redirect to the index page

if __name__ == "__main__":
    app.run(debug=True)
