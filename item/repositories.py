from domains.item.repository import ItemRepository
from domains.item.entity import Item as DomainItem
from .models import Item as DjangoItem

class DjangoItemRepository(ItemRepository):
    def get_item_by_id(self, item_id: int) -> DomainItem:
        try:
            db_item = DjangoItem.objects.get(id=item_id)
            return DomainItem(id=db_item.id, 
                            name=db_item.name, 
                            description=db_item.description, 
                            price=db_item.price)
        
        except DjangoItem.DoesNotExist:
            return None