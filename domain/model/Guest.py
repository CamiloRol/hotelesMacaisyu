from domain.model.User import User


class Guest(User):

    def __init__(self, id, name, last_name, email, password, status, origin, occupation, check_in, check_out):
        super.__init__(id, name, last_name, email, password, status)
        self.origin = origin
        self.occupation = occupation
        self.check_in = check_in
        self.check_out = check_out

    def room_book(self, room):
        if room.available:
            room.mark_available(False)
            return f"Habitación {room.room_number} reservada correctamente a {self._name}"
        else:
            return f"Habitación {room.room_number} no se encuentra disponible"

    def __str__(self):
        return f"Húesped: {self._name} {self._last_name}, Origen: {self.origin}, Ocupacion {self.occupation}, Fecha entrada: {self.check_in}, Fecha salida: {self.check_out}"
