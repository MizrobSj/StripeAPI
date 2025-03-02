from .repository import ItemRepository
from domains.stripe.payment import StripeProvider
class ItemService:
    def __init__(self, item_repository: ItemRepository, stripe_provider: StripeProvider):
        self.item_repository = item_repository
        self.stripe_provider = stripe_provider
    
    def create_chekout_session(self, id: int) -> str:
        item = self.item_repository.get_item_by_id(id)
        if item is None:
            raise ValueError("Item not found")
        
        session = self.stripe_provider.create_checkout_session(item)
        return session.id

         
        
