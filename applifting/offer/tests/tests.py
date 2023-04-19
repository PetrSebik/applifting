import factory.django
from rest_framework.test import APITestCase, APIClient
from django.db.models import signals
from .factory import (
    OfferFactory
)


class GetOffersTestCase(APITestCase):

    @factory.django.mute_signals(signals.post_save)
    def setUp(self):
        self.client = APIClient()
        self.offer1 = OfferFactory()
        self.offer2 = OfferFactory()

    @factory.django.mute_signals(signals.post_save)
    def test_get_offers(self):
        response = self.client.get('/api/offers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    # TODO here we should add more tests like these above. But I consider these as enough tests for an EXAMPLE project

