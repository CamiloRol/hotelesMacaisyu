from domain.model.Guest import Guest

class GuestService:

    def __init__(self):
        self.guest = Guest
        self.register_data = []

    def create_guest(self, guest):
        guest.get_id = self.register_data[0]
        guest.get_name = self.register_data[1]
        guest.get_last_name = self.register_data[2]
        guest.get_phone = self.register_data[3]
        guest.get_email = self.register_data[4]
        guest.get_password = self.register_data[5]
        guest.get_status = self.register_data[6]

    def print_data_service(self):

        for data in self.register_data:
            print(data)

