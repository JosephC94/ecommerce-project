from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    def test_str(self):
        test_name = Product(name='a Product')
        self. assertEqual(str(test_name), 'a Product')
