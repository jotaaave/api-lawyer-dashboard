# from interfaces.user_repository_type import UserRepositoryInterface

class UserMemoryRepository:
    __users = []

    def add(self, user):
        user = self.find_by_email(user['email'])

        if user:
            return

        self.__users.append(user)
        return {
            user
        }

    def find_by_email(self, email: str):
        return next((user for user in self.__users if user["email"] == email), None)

    def find_by_id(self, id):
        return next((user for user in self.__users if user["id"] == id), None)
