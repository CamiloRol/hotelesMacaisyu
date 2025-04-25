from domain.model.Employee import Employee

class EmployeeService:
    register_employee = []

    def __init__(self):
        self.employee = Employee(None, None,None,None, None,None, None )

    def create_employee(self, employee):
        employee.id_employee = self.register_data[0]
        employee.name = self.register_data[1]
        employee.last_name = self.register_data[2]
        employee.email = self.register_data[3]
        employee.password = self.register_data[4]
        employee.status = self.register_data[5]
        employee.salary = self.register_data[6]

    def print_employee_data(self=None):
        for employee in self.register_employee:
            print(employee)






