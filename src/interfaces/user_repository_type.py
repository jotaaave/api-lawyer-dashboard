from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    @abstractmethod
    def add():
        pass

    @abstractmethod
    def find_by_email():
        pass

    @abstractmethod
    def find_by_id():
        pass