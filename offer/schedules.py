from applifting.product.models import Product
from applifting.offer.models import Offer
from .api import APIClient, APIError


def update_offers():
    client = APIClient()
    for product in Product.objects.all():
        try:
            offers = client.get_product_offers(product.id)
        except APIError:
            continue
        Offer.objects.filter(product=product).delete()
        for offer in offers:
            new_offer = Offer(
                product=product,
                id=offer['id'],
                price=offer['price'],
                items_in_stock=offer['items_in_stock']
            )
            new_offer.save()
