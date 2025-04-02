class Room:
    def __init__(self, room_number, room_type, available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.available = available

    def mark_available(self, available):
        self.available = available

    def __str__(self):
        availability = "Disponible" if self.available else "No disponible"
        return f"Número {self.room_number}, Tipo: {self.room_type}, Estado: {availability}"


room1 = Room(101, "Single", True)
print(room1)  # Imprime: Número 101, Tipo: Single, Estado: Disponible

room1.mark_available(False)
print(room1)  # Imprime: Número 101, Tipo: Single, Estado: No disponible
