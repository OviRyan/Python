class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id


class PermanentEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class ContractEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


permanent_employee = PermanentEmployee("Ovi", 1824, 5000)  
contract_employee = ContractEmployee("Osai", 1824, 20, 160)  

print(f"Permanent Employee - Name: {permanent_employee.name}, ID: {permanent_employee.id}, Salary: {permanent_employee.calculate_salary()}")
print(f"Contract Employee - Name: {contract_employee.name}, ID: {contract_employee.id}, Salary: {contract_employee.calculate_salary()}")
