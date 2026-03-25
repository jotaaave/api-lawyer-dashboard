from app.errors import InvalidFormBody
from random import randrange

class Client:
    def create_client(data):
        print(data.get("name"))

        if not data.get('name'):
            raise InvalidFormBody

        client = {
            "name": data.get("name"),
            "id": randrange(1, 200) * len(data.get("name"))
        }

        return client