from domain.model.Guest import Guest
from application.GuestService import GuestService
from application.Guestinput import GuestInput
from application.RoomInput import RoomInput
from repository.connection.MysqlDataHandler import Conexion


class MenuApp:

    def __init__(self):
        self.db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel')
        self.db.connection()
        self.guest= Guest(None, None,None,None,None,None,None,None,None)
        self.guest_service= GuestService()
        self.guest_input= GuestInput()


    def init_app(self=None):
        init = (int(input("Presione 1 para inicializar ")))

        while init != 0:

            option = int(input(" 1. Login \n 2. Registro \n 3. Salir \n"))

            match option:
                case 1:
                    print("login")
                case 2:
                    print("Registro")
                    self.guest_input.register(self.guest, self.db)
                case 3:
                    init = 0


    def reservation_menu(self=None):
        option = int(input(" 1. Consultar reserva \n 2. Reservar \n 3. Salir \n"))

        match option:
            case 1:
                print("haz consultado exitosamente")
            case 2:
                print("Proceso de reserva")
            case 3:
                init = 0
                return init

    def room_menu(self=None):
        option = int(input("1. Listar habitaciones, 2.Buscar por número, 3. Registrar nueva habitación 4.Actualizar disponibilidad 5.Eliminar habitación"))

        match option:
            case 1:
                print("Listar habitaciones")
                self.roomInput.print_data()


