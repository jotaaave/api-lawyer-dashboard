from interfaces.client_repository_type import ClientRepositoryInterface

class ClientMemoryRepository(ClientRepositoryInterface):
    __clients = []

    def add(self, client):
        self.__clients.append(client)

    def get_all(self):
        return self.__clients
    
    def get_one_by_id(self, id):
        return next((c for c in self.__clients if c['id'] == id), None)
    

clientMemoryRepository = ClientMemoryRepository()