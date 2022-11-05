from django.test import TestCase
from rest_framework.test import APITestCase

from seller.models import Seller


class SellerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.seller_data = {
            "username": "Alex",
            "password": "abcd",
            "first_name": "alexandre",
            "last_name": "alves",
            "is_seller": True,
        }

        cls.seller = Seller.objects.create(**cls.seller_data)

    def test_first_and_last_name_max_length(self):
        max_length_first = self.seller._meta.get_field("first_name").max_length
        max_length_last = self.seller._meta.get_field("first_name").max_length
        self.assertEqual(max_length_first, 50)
        self.assertEqual(max_length_last, 50)

    def test_seller_fields(self):
        self.assertEqual(self.seller.username, self.seller_data["username"])
        self.assertEqual(self.seller.first_name, self.seller_data["first_name"])
        self.assertEqual(self.seller.last_name, self.seller_data["last_name"])
        self.assertEqual(self.seller.is_seller, self.seller_data["is_seller"])


class SellerViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.seller_data = {
            "username": "Alex",
            "password": "abcd",
            "first_name": "alexandre",
            "last_name": "alves",
            "is_seller": True,
        }

    def test_create_user_seller(self):
        response = self.client.post("/api/accounts/", self.seller_data)
        self.assertEqual(response.status_code, 200)
