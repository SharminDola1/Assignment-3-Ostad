# Employee Salary Management System
# Concepts used: Functions, Parameters, Return Statements, File Handling ('r', 'a')


def read_records(filename):
    """Reads all lines from the specified text file and returns them as a list."""
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        # Return an empty list if the file does not exist yet
        return []


def format_employee_data(name, emp_id, salary):
    """Formats employee details into the required string structure."""
    return f"{name} | {emp_id} | {salary}\n"


def add_employee(filename, name, emp_id, salary):
    """Appends a new employee record to the text file."""
    record = format_employee_data(name, emp_id, salary)
    with open(filename, "a") as file:
        file.write(record)
    return "Employee Added Successfully"


def view_employees(filename):
    """Fetches and displays all employee records from the file."""
    records = read_records(filename)
    if not records:
        print("\nNo employee records found.")
    else:
        print("\n--- Employee Records ---")
        for record in records:
            print(record.strip())


def get_employee_input():
    """Prompts the user for employee details and returns them."""
    name = input("\nEnter Name: ").strip()
    emp_id = input("Enter ID: ").strip()
    salary = input("Enter Salary: ").strip()
    return name, emp_id, salary


def display_menu():
    """Displays the main menu options."""
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")


def main():
    """Main function to control the program flow."""
    filename = "employees.txt"

    while True:
        display_menu()
        choice = input("\nChoose Option: ").strip()

        if choice == "1":
            name, emp_id, salary = get_employee_input()
            if name and emp_id and salary:
                status = add_employee(filename, name, emp_id, salary)
                print(f"\n{status}")
            else:
                print("\nError: All fields (Name, ID, Salary) are required.")

        elif choice == "2":
            view_employees(filename)

        elif choice == "3":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid option! Please enter 1, 2, or 3.")


# Run the program
if _name_ == "_main_":
    main()


