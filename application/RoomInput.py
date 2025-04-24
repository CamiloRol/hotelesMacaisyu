from domain.model.Room import Room
from repository.persistence.RoomRepository import RoomRepository


class RoomInput:
    def __init__(self):
        self.room = Room
        self.room_repository = RoomRepository()

    def register(self, room, db):

        room_number = int(input("Ingrese el número de habitación:"))
        self.room.get_room_number(room_number)
        room_type = input("Ingrese el tipo de habitación")
        self.room.get_type

        self.room_repository.create_room_repository( None, room, db)




    # Metodo para crear habitacion
    def add_new_room(self):
        try:
            number = int(input("Ingrese el numero de habitación"))
            self.room_service.register_room.append(number)
            type = input("Ingrese el tipo de habitación")
            self.room_service.register_room.append(type)
        except ValueError:
            print("El número para crear habitación debe ser entero")

    # Metodo para reservar habitacion
    def book_room(self):
        try:
            number = int(input("Ingrese el número de la habitación que desea reservar: "))
            if self.room_service.book_room(number):
                print(f"Habitacion {number} reservada exitosamete")
            else:
                print(f"No se encontró la habitacion {number}")
        except ValueError:
            print("Eror al ingresar número de habitación")

    # Metodo para mostrar las habitaciones creadas
    def show_all_rooms(self):
        self.room_service.print_all_rooms()

