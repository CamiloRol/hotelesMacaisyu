from application.RoomService import RoomService
from domain.model.Room import Room
from repository.persistence.RoomRepository import RoomRepository


class RoomInput:
    def __init__(self):
        self.room = Room(None, None)
        self.room_repository = RoomRepository()
        self.room_service = RoomService()

    def register(self, room, db):
        room_number = input("Ingrese su número de habitación")
        self.room.room_number = room_number
        room_type = input("Ingrese tipo de habitación")
        self.room.room_type = room_type

        self.room_repository.create_room_repository( None, room, db)

    def print_data(self):
        self.room_service.print_all_rooms()


