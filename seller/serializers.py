from rest_framework import serializers
from .models import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "is_seller",
            "date_joined",
            "is_superuser",
            "is_active",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user_obj = Seller.objects.create_user(**validated_data)

        return user_obj
