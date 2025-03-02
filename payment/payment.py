from django.conf import settings
import stripe
from domains.stripe.payment import StripeProvider

stripe.api_key = settings.STRIPE_SECRET_KEY
# stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'

class Payment(StripeProvider):
    def create_checkout_session(self, item):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {   'price_data': {
                            'currency': 'usd',
                            'unit_amount': int(float(item.price) * 100),
                            'product_data':{
                                'name': item.name,
                                'description': item.description
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url='http://localhost:8000/success',
                cancel_url='http://localhost:8000/cancel',
            )
            return checkout_session
                
                  
        except Exception as e:
            raise Exception(f"Ошибка при создании сессии Stripe: {str(e)}")
        