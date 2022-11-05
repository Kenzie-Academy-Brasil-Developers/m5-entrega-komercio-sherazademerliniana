from django.test import TestCase
from rest_framework.test import APITestCase

from seller.models import Seller
from product.models import Product


class ProductRelationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product_data = {
            "description": "Smartband XYZ 3.0",
            "price": 100.99,
            "quantity": 15,
        }

        cls.product_data2 = {
            "description": "XYZ 3.0",
            "price": 102.99,
            "quantity": 13,
        }

        cls.seller_data = {
            "username": "Alex",
            "password": "abcd",
            "first_name": "alexandre",
            "last_name": "alves",
            "is_seller": True,
        }

        cls.seller_data2 = {
            "username": "Truta",
            "password": "abcd",
            "first_name": "Truta",
            "last_name": "alves",
            "is_seller": True,
        }

        cls.seller = Seller.objects.create(**cls.seller_data)
        cls.seller2 = Seller.objects.create(**cls.seller_data2)
        cls.product = Product(**cls.product_data)
        cls.product2 = Product(**cls.product_data)

    def test_many_to_one_relation_with_seller(self):
        self.product.seller = self.seller
        self.product.save()
        self.product2.seller = self.seller
        self.product2.save()

        self.assertIs(self.product.seller, self.seller)
        self.assertIs(self.product2.seller, self.seller)

    def test_animal_not_more_group(self):
        self.product.seller = self.seller
        self.product.save()
        self.product2.seller = self.seller
        self.product2.save()

        self.product.seller = self.seller2
        self.product.save()
        self.product2.seller = self.seller2
        self.product2.save()

        self.assertIsNot(self.product.seller, self.seller)
        self.assertIsNot(self.product2.seller, self.seller)
        self.assertIs(self.product.seller, self.seller2)
        self.assertIs(self.product2.seller, self.seller2)


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product_data = {
            "description": "Smartband XYZ 3.0",
            "price": 100.99,
            "quantity": 15,
        }

        cls.seller_data = {
            "username": "Alex",
            "password": "abcd",
            "first_name": "alexandre",
            "last_name": "alves",
            "is_seller": True,
        }

        cls.seller = Seller.objects.create(**cls.seller_data)
        cls.product = Product.objects.create(**cls.product_data, seller=cls.seller)

    def test_product_fields(self):
        self.assertEqual(self.product.description, self.product_data["description"])
        self.assertEqual(self.product.price, self.product_data["price"])
        self.assertEqual(self.product.quantity, self.product_data["quantity"])

