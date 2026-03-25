from abc import ABC, abstractmethod

class ClientRepositoryInterface(ABC):
    @abstractmethod
    def get_all():
        pass

    @abstractmethod
    def add():
        pass

    @abstractmethod
    def get_one_by_id():
        pass

    