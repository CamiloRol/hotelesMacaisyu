class Reservation:

    def __init__(self, guest_id, room_number, booking_date):
        self.guest_id = guest_id
        self.room_number = room_number
        self.booking_date = booking_date

    def __str__(self):
        return (
            f"Reservation Details:\n"
            f"  - Guest ID     : {self.guest_id}\n"
            f"  - Room Number  : {self.room_number}\n"
            f"  - Booking Date : {self.booking_date}"
        )
