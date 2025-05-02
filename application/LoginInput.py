from repository.persistence.GuestRepository import GuestRepository
from repository.persistence.LoginRepository import LoginRepository


class LoginInput:

    def __init__(self):
        self.login_repository= LoginRepository()
        self.guest_repository= GuestRepository()

    def loginProc(self, db):
        user= input("Ingrese usuario: ")
