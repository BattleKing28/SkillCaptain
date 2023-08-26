import unittest
from day9 import Product, Cart

# from day9 import add_to_cart, remove_from_cart, display_cart


class TestAddToCart(unittest.TestCase):
    def setUp(self):
        testProduct = Product("", "", "")
        testCart = Cart("")

    def test_add_empty_product(self):
        res = Cart.add_to_cart(self.testProduct)
        self.assertEqual(res, {})
