import datetime
import pytz
from uuid import uuid4
from django.db import models


class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, db_index=True)
    product = models.ForeignKey('product.product', on_delete=models.CASCADE, related_name='offers')
    price = models.IntegerField()
    items_in_stock = models.IntegerField()


class APIToken(models.Model):
    token = models.CharField(max_length=256)
    exp = models.DateTimeField(blank=True)

    def load_exp(self, unix: int):
        self.exp = datetime.datetime.fromtimestamp(unix).astimezone(tz=pytz.timezone('Europe/Prague'))

    def is_valid(self) -> bool:
        return datetime.datetime.now(tz=pytz.timezone('Europe/Prague')) < self.exp
