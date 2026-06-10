from db import get_connection

def add_employee(name, dept, salary, date):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO employees
    (name, department, salary, joining_date)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, dept, salary, date))

    conn.commit()
    conn.close()

    print("Employee Added Successfully")


def view_employees():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def update_employee(emp_id, salary):
    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE employees SET salary=%s WHERE emp_id=%s"

    cursor.execute(query, (salary, emp_id))

    conn.commit()
    conn.close()

    print("Employee Updated Successfully")


def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM employees WHERE emp_id=%s"

    cursor.execute(query, (emp_id,))

    conn.commit()
    conn.close()

    print("Employee Deleted Successfully")