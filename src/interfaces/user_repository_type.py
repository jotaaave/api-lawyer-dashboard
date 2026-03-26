from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    @abstractmethod
    def add_user(user):
        pass

    @abstractmethod
    def find_by_email(email: str):
        pass

    @abstractmethod
    def find_by_id(id: str):
        pass