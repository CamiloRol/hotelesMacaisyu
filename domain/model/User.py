class User:

    def __init__(self, id, name, last_name, email, password, status):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._status = status


    @property
    def get_id(self):
        return self._id

    @get_id.setter
    def set_id(self, id):
        self._id = id