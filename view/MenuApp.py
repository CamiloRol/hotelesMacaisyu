from application.Guestinput import Guestinput
from domain.model.Guest import Guest
from domain.service.GuestService import GuestService


class MenuApp:

    def __init__(self):
        self.guest = Guest
        self.guest_service = GuestService
        self.guest_input = Guestinput

    def init_app(self):
        init = (int(input("Presione 1 para inicializar")))

        while  init != 0:

            option = int(input("1. Login \n2. Register \n3. Exit"))

            match option:
                case 1:
                    print("Login")
                case 2:
                    print("Register")
                    self.guest_input.register()
                    self.guest_service.createGuest()
                case 3:
                    print("Exit")