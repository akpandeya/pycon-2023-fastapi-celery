from abc import ABC, abstractmethod
from uuid import UUID


class BaseGetService(ABC):
    @abstractmethod
    def get_by_id(self, id: UUID):
        pass
