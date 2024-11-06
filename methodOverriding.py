class Employee:
    def calculate_salary(self):
        print("Calculating salary for a generic employee.")

# This is a subclass
class Manager(Employee):
    def calculate_salary(self):
        print("Calculating salary specifically for a manager with additional benefits.")

employee = Employee()
manager = Manager()

employee.calculate_salary()
manager.calculate_salary()
