import requests
import jwt
from typing import TYPE_CHECKING, List
from django.conf import settings
from .models import APIToken

while TYPE_CHECKING:
    from applifting.product.models import Product


class APIError(Exception):
    """base exception for the API errors"""


class APIClient:
    """API client for the Applifting offers external API"""

    def __init__(self):
        api_token = APIToken.objects.order_by('-exp').first()
        if api_token and api_token.is_valid():
            self.access_token = api_token.token
        else:
            new_token = self.auth()
            payload = jwt.decode(
                new_token,
                algorithms="HS256",
                options={"verify_signature": False}
            )
            api_token = APIToken(token=new_token)
            api_token.load_exp(payload.get('expires', 0))
            api_token.save()
            self.access_token = new_token

    def auth(self):
        """get a valid access token for the other authenticated requests"""
        headers = {"Bearer": settings.REFRESH_TOKEN}
        resp = requests.post(url=f"{settings.EXTERNAL_API_URL}/auth", headers=headers)
        if resp.status_code != 201:
            raise APIError
        return resp.json().get('access_token')

    def register_products(self, product: 'Product') -> bool:
        """
        :param product: product to register
        :return: bool, True if action was successful
        """
        headers = {"Bearer": self.access_token}
        body = {
            "id": str(product.id),
            "name": product.name,
            "description": product.description
        }
        resp = requests.post(url=f"{settings.EXTERNAL_API_URL}/products/register", headers=headers, json=body)
        if resp.status_code == 401 and resp.json().get('details') == 'Access token expired':
            self.auth()
            return self.register_products(product=product)
        if resp.status_code != 201:
            raise APIError
        return True

    def get_product_offers(self, id: str) -> List[dict]:
        """
        :param id: id of the product to get the offers to
        :return: list of dictionaries with the product offers
        """
        headers = {"Bearer": self.access_token}
        resp = requests.get(url=f"{settings.EXTERNAL_API_URL}/products/{id}/offers", headers=headers)
        if resp.status_code == 401 and resp.json().get('details') == 'Access token expired':
            self.auth()
            return self.get_product_offers(id=id)
        if resp.status_code != 200:
            raise APIError
        return resp.json()
