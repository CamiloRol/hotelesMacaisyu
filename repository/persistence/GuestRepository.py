from domain.model.Guest import Guest
from repository.connection.MysqlDataHandler import dbDataHandler


class GuestRepository:

    def __init__(self):
        self.guest = Guest

    def create_guest_repository(self, guest, db):
        query = "INSERT INTO guest (id, name, last_name, phone, email, password, status, origin, occupation) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (guest.get_id, guest.get_name, guest.get_last_name, guest.get_phone, guest.get_email, guest.get_password, guest.get_status)
        db.execute_query(query, values)