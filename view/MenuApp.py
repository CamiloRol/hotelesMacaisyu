from domain.model.Guest import Guest
from application.GuestService import GuestService
from application.Guestinput import GuestInput
from application.RoomInput import RoomInput
from repository.connection.MysqlDataHandler import Conexion
from domain.model.Room import Room


class MenuApp:

    def __init__(self):
        self.db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel')
        self.db.connection()
        self.guest= Guest(None, None,None,None,None,None,None,None,None)
        self.guest_service= GuestService()
        self.guest_input= GuestInput()
        self.room_input = RoomInput()
        self.room = Room(None, None)

    def init_app(self):
        init = (int(input("Presione 1 para inicializar ")))

        while init != 0:

            option = int(input(" 1. Login \n 2. Registro \n 3. Reservar \n 4. Salir \n"))

            match option:
                case 1:
                    print("login")
                case 2:
                    print("Registro")
                    self.guest_input.register(self.guest, self.db)
                case 3:
                    self.reservation_menu()
                case 4:
                    init = 0


    def reservation_menu(self):
        option = int(input(" 1. Consultar reserva \n 2. Reservar \n 3. Salir \n"))

        match option:
            case 1:
                print("haz consultado exitosamente")
            case 2:
                print("Proceso de reserva")
                self.room_menu()
            case 3:
                init = 0
                return init

    def room_menu(self):
        option = int(input(" 1. Listar habitaciones \n 2.Buscar por número \n 3. Registrar nueva habitación \n 4.Actualizar disponibilidad \n 5.Eliminar habitación"))

        match option:
            case 1:
                print("Listar habitaciones")
                self.room_input.print_data()
            case 2:
                print("Encontraste la habitación")
            case 3:
                self.room_input.register(self.room, self.db)


