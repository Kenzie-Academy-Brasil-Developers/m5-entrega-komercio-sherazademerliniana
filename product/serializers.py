from rest_framework import serializers

from seller.serializers import SellerSerializer
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "description",
            "price",
            "quantity",
            "is_active",
            "seller",
        ]


class ProductDetailedSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["id"]
        read_only_fields = ["seller"]
