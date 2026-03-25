from interfaces.client_repository_type import ClientRepositoryInterface
from models.client_model import Client
from app.errors import InvalidFormBody

class ClientService:
    def __init__(self, client_repository: ClientRepositoryInterface):
        self.db = client_repository

    def get_all(self):
        return self.db.get_all()
    
    def get_client_by_id(id: int):
        
    
    def add(self, data):
        try:
            client = Client.create_client(data)
            self.db.add(client)

            return {
                "client": client
            }
        except InvalidFormBody:
            raise InvalidFormBody
        except Exception as e:
            return e
