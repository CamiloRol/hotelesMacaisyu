from domain.model.User import User


class Guest(User):

    def __init__(self, id, name, last_name, email, password, status, origin, occupation):
        super.__init__(id, name, last_name, email, password, status)
        self.origin = origin
        self.occupation = occupation