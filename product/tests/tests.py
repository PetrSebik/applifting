import factory.django
from rest_framework.test import APITestCase, APIClient
from django.db.models import signals
from .factory import (
    ProductFactory
)
from applifting.product.models import Product


class CreateProductTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    @factory.django.mute_signals(signals.post_save)
    def test_create_product(self):
        data = {
            "name": "my product",
            "description": "test product description",
        }
        response = self.client.post('/api/products/', data=data)
        products = Product.objects.first()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(products.name, data["name"])
        self.assertEqual(products.description, data["description"])

    def test_create_product_fail(self):
        data = {
            "name": "my product"
        }
        response = self.client.post('/api/products/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['description'][0], 'This field is required.')


class ProductTestCase(APITestCase):

    @factory.django.mute_signals(signals.post_save)
    def setUp(self):
        self.client = APIClient()
        self.product1 = ProductFactory()
        self.product2 = ProductFactory()

    def test_get_all_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    @factory.django.mute_signals(signals.post_save)
    def test_patch_product(self):
        data = {
            "description": "new description"
        }
        response = self.client.patch(f'/api/products/{self.product1.id}/', data=data)
        self.assertEqual(response.status_code, 200)
        product = Product.objects.filter(id=self.product1.id).first()
        self.assertIsNotNone(product)
        self.assertEqual(product.description, data['description'])

    # TODO here we should add more tests like these above. But I consider these as enough tests for an EXAMPLE project
