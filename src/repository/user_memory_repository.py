from interfaces.user_repository_type import UserRepositoryInterface

class UserMemoryRepository(UserRepositoryInterface):
    __users = []

    def add_user(self, user):
        user_in_database = self.find_by_email(user['email'])

        if user_in_database:
            return

        self.__users.append(user)

        return user

    def find_by_email(self, email: str):
        return next((user for user in self.__users if user["email"] == email), None)

    def find_by_id(self, id):
        return next((user for user in self.__users if user["id"] == id), None)
    
userMemoryRepository = UserMemoryRepository()
