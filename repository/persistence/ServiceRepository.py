from domain.model.Services import Services


class ServiceRepository:
    def __init__(self):
        self.service = Services

    def create_service_repository(self, service, db):

        query = "INSERT INTO Services (id_service, description, price) VALUES (%s, %s, %s)"
        values = (service.id_service, service.description, service.price)
        db.execute_query(query, values)