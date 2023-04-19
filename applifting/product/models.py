from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from applifting.offer.api import APIClient
from uuid import uuid4


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, db_index=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)


@receiver(post_save, sender=Product)
def register_product(sender, instance, *args, **kwargs):
    client = APIClient()
    client.register_products(product=instance)
    client.get_product_offers(id=instance.id)
