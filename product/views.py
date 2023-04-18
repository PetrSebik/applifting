from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer


class ListCreateProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.filter()


class RetrieveUpdateDestroyProductView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.filter()
