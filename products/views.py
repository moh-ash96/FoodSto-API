from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAdminUser


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

