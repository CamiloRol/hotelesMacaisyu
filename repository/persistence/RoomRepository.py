from domain.model.Room import Room


class RoomRepository:
    def __init__(self):
        pass

    def create_room_repository(self, room_number, room_type, db):
        # Crear una instancia de Room
        room = Room(room_number, room_type)

        # Usar la instancia para acceder a las propiedades
        query = "INSERT INTO room (room_number, room_type) VALUES (%s, %s)"
        values = (room.get_room_number, room.get_type)
        db.execute_query(query, values)
