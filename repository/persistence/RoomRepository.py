import dbm

from domain.model.Room import Room


class RoomRepository:
    def __init__(self):
        self.room = Room

    def create_room_repository(self, room, db):
        # Usar la instancia para acceder a las propiedades
        query = "INSERT INTO Room (room_number, room_type, available) VALUES (%s, %s, %s)"
        values = (room.room_number, room.room_type, room.available)
        db.execute_query(query, values)

    def find_all(self, db):
        query = "SELECT * FROM Room"
        return db.execute_query(query)

    def find_by_room_numer(self, room_number, db):
        query = "SELECT * FROM Room WHERE room_number = %s"
        values = (room_number,)
        return db.execute_query(query, values)

    def find_available(self, db):
        query = "SELECT * FROM Room WHERE available = %s"
        values = ('AVAILABLE',)  # Usamos AVAILABLE porque ese es el valor de la columna
        return db.execute_query(query, values)

    def update_availability(self, room_number, availability, db):
        query = 'UPDATE Room SET available = %s WHERE room_number = %s'
        values = (availability, room_number)
        db.execute_query(query, values)

    def delete(self, room_numer, db):
        query = "DELETE FROM Room WHERE room_numer = %s"
        values = (room_numer,)
        db.execute_query(query,values)