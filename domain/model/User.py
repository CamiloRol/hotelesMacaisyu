class User:

    def __init__(self, id, name, last_name, phone, email, password, status):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._phone = phone
        self._email = email
        self._password = password
        self._status = status

    @property
    def get_id(self):
        return self._id

    @get_id.setter
    def set_id(self, id):
        self._id = id

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def set_name(self, name):
        self._name = name

    @property
    def get_last_name(self):
        return self._last_name

    @get_last_name.setter
    def set_last_name(self, last_name):
        self._last_name = last_name

    @property
    def get_phone(self):
        return self._phone

    @get_phone.setter
    def set_email(self, phone):
        self._phone = phone

    @property
    def get_email(self):
        return self._email

    @get_email.setter
    def set_email(self, email):
        self._email = email

    @property
    def get_password(self):
        return self._password

    @get_password.setter
    def set_password(self, password):
        self._password = password

    @property
    def get_status(self):
        return self._status

    @get_status.setter
    def set_status(self, status):
        self._status = status

    def __str__(self):
        return f"User: {self._name} {self._last_name}, Email: {self._email}, Status: {self._status}"