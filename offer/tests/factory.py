import factory
from faker import Faker
from applifting.offer.models import Offer
from applifting.product.tests.factory import ProductFactory

Faker.seed(0)
fake = Faker(locale=['en_GB'])


class OfferFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Offer

    product = factory.SubFactory(ProductFactory)
    price = fake.random_number()
    items_in_stock = fake.random_number()
