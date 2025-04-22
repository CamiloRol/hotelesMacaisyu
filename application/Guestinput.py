from domain.model.Guest import Guest
from repository.persistence.GuestRepository import GuestRepository


class GuestInput:

    def __init__(self):
        self.guest = Guest(None, None, None, None, None, None, None, None, None,)
        self.guest_repository = GuestRepository

    def register(self, guest, db):

        id = int(input("Ingrese su numero de documento de identidad:"))
        self.guest.get_id(id)
        name = input("Ingrese su nombre")
        self.guest.get_name(name)
        last_name = input("Ingrese su apellido")
        self.guest.get_last_name(last_name)
        phone = input("Ingrese su telefono")
        self.guest.get_phone(phone)
        email = input("Ingrese su correo")
        self.guest.get_email(email)
        password = input("Ingrese su contraseña")
        self.guest.get_password(password)
        status = input("Seleccione el estado")
        self.guest.get_status(status)
        origin = input("Ingrese su ciudad de origen")
        self.guest.get_origin(origin)
        occupation = input("Ingrese su ocupacion")
        self.guest.get_occupation(occupation)

        self.guest_repository.create_guest_repository( None, guest, db)
