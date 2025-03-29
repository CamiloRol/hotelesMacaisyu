from domain.model.User import User


class Employee(User):
    def __init__(self, id, name, last_name, email, password, status):
        super.__init__(id, name, last_name, email, password, status)