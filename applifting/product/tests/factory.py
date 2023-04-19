import factory
from faker import Faker
from applifting.product.models import Product

Faker.seed(0)
fake = Faker(locale=['en_GB'])


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = fake.text(64)
    description = fake.text(256)
