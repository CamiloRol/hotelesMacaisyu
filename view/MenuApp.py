from application.GuestInput import GuestInput
from domain.model.Guest import Guest
from application.GuestService import GuestService
from repository.connection.MysqlDataHandler import dbDataHandler


class MenuApp:

    db = dbDataHandler(host= 'localhost', port=3306, user="root", password="", database="hotel")
    db.db_conec()

    def __init__(self):
        self.guest = Guest
        self.guest_service = GuestService()
        self.guest_input = GuestInput()

    def init_app(self):
        init = (int(input("Presione 1 para inicializar")))

        while  init != 0:

            option = int(input("1. Login \n2. Register \n3. Exit"))

            match option:
                case 1:
                    print("Login")
                case 2:
                    print("Register")
                    self.guest_input.register(guest, db)
                case 3:
                    print("Exit")