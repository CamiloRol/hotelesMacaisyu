from domain.model.User import User


class Employee(User):
    def __init__(self, id, name, last_name, email, password, status, salary, address):
        super.__init__(id, name, last_name, email, password, status)
        self.salary = salary
        self.address = address

