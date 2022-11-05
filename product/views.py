from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.authentication import TokenAuthentication

from product.models import Product
from product.permissions import IsOwner, IsSeller
from product.serializers import (
    ProductDetailedSerializer,
    ProductListSerializer,
    ProductSerializer,
)
from utils.mixins import SerializerByMethodMixin

# Create your views here.
class ProductView(SerializerByMethodMixin, ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSeller]

    queryset = Product.objects.all()
    serializer_map = {
        "GET": ProductSerializer,
        "POST": ProductDetailedSerializer,
    }
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(seller=self.request.user)


class ProductDetailView(SerializerByMethodMixin, RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    serializer_map = {
        "GET": ProductListSerializer,
        "PATCH": ProductDetailedSerializer,
    }
