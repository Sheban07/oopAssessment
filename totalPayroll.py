class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"{self.name}, ${self.salary}"


class Payroll:
    def __init__(self, employees=None):
        if employees is None:
            employees = []
        self.employees = employees

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_payroll(self):
        total = sum(employee.salary for employee in self.employees)
        return total

emp1 = Employee("Ann",  50000)
emp2 = Employee("Omar",  30000)

payroll = Payroll([emp1, emp2])
print(f"Total Payroll: ${payroll.total_payroll()}")
