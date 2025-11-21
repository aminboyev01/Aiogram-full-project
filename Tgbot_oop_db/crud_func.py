import sqlite3
from contextlib import closing

def get_connection(database_path):
    return closing(sqlite3.connect(database_path))

def create_employee(database_path, first_name, last_name, email, job_id, salary, hire_date, phone_number=None, manager_id=None, department_id=1):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO employees (first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id))
        connection.commit()
        return cursor.lastrowid

def get_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id=?", (employee_id,))
        return cursor.fetchone()

def update_employee(database_path, employee_id, salary=None, email=None):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        if salary:
            cursor.execute("UPDATE employees SET salary=? WHERE employee_id=?", (salary, employee_id))
        if email:
            cursor.execute("UPDATE employees SET email=? WHERE employee_id=?", (email, employee_id))
        connection.commit()

def delete_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE employee_id=?", (employee_id,))
        connection.commit()

database = "sample-database.db"

emp_id = create_employee(
    database,
    first_name="Shohrux",
    last_name="Aminboyev",
    email="shohrux.aminboyev@gmail.com",
    job_id=4,
    salary=123000,
    hire_date="2025-10-28",
    phone_number=998909999999,
    manager_id=None,
    department_id=1
)

print(get_employee(database, emp_id))
update_employee(database, emp_id, salary=150000, email="sh.aminboyev@company.uz")
print(get_employee(database, emp_id))
delete_employee(database, emp_id)
print(get_employee(database, emp_id))
