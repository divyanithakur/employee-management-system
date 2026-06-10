from operations import *

while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = int(input("Enter Salary: "))
        date = input("Enter Joining Date (YYYY-MM-DD): ")

        add_employee(name, dept, salary, date)

    elif choice == "2":
        view_employees()

    elif choice == "3":

        emp_id = int(input("Enter Employee ID: "))
        salary = int(input("Enter New Salary: "))

        update_employee(emp_id, salary)

    elif choice == "4":

        emp_id = int(input("Enter Employee ID: "))
        delete_employee(emp_id)

    elif choice == "5":

        emp_id = int(input("Enter Employee ID: "))
        search_employee(emp_id)

    elif choice == "6":
        print("Good Bye")
        break

    else:
        print("Invalid Choice")