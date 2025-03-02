from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.conf import settings

from .repositories import DjangoItemRepository
from domains.item.entity import Item as DomainItem
from .models import Item as DjangoItem
from domains.item.service import ItemService
from payment.payment import Payment

def item_deteil(request, id):
    item = get_object_or_404(DjangoItem, id=id)
    context = {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY, 
    }

    return render(request, 'item_detail.html', context)


def buy_item(request, id):
    repository = DjangoItemRepository()
    payment = Payment()
    service = ItemService(item_repository=repository, stripe_provider=payment)
    try:
        session_id = service.create_chekout_session(id)
    except ValueError as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse({'session_id': session_id})
def success_view(request):
    return HttpResponse("Payment successful!")

def cancel_view(request):
    return HttpResponse("Payment canceled!")