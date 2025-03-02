from abc import ABC, abstractmethod

class StripeProvider(ABC):
    @abstractmethod
    def create_checkout_session(self, item) -> object:
        pass