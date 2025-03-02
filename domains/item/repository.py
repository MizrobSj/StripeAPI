from abc import ABC, abstractmethod
from .entity import Item

class ItemRepository(ABC):
    @abstractmethod
    def get_item_by_id(self, id) -> Item:
        pass
    