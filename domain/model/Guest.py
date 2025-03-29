from domain.model.User import User


class Guest(User):

    def __init__(self, id, name, last_name, email, password, status, origin, occupation):
        super().__init__(id, name, last_name, email, password, status)
        self._origin = origin
        self._occupation = occupation


@property
def get_origin(self):
    return self._origin

@get_origin.setter
def set_origin(self, origin):
    self._origin = origin

@property
def get_occupation(self):
    return self._occupation

@get_occupation.setter
def set_occupation(self, occupation):
    self._occupation = occupation