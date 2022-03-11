class Payroll:
    def __init__(self):
        self.employee_list = []

    def __add__(self, employee):
        self.employee_list.append(employee)

    def print(self):
        for employee in self.employee_list:
            print(f"{employee.full_name} \t ${employee.get_salary()}")