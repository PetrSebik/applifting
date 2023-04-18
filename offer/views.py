from rest_framework import generics, permissions
from applifting.product.models import Product
from .serializers import ProductOffersSerializer


class ListOffersView(generics.ListAPIView):
    serializer_class = ProductOffersSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.filter()
