import unittest
from day9 import Product, Cart

# from day9 import add_to_cart, remove_from_cart, display_cart


class CartFunctionality(unittest.TestCase):
    def setUp(self):
        self.prod1 = Product("Bat", 25.99, 2)
        self.prod2 = Product("T shirt", 35.99, 20)
        self.cart1 = Cart("Mark")

    def test_add_valid_product(self):
        self.cart1.add_to_cart(self.prod1)
        self.assertIn(self.prod1, self.cart1.cart_items)

    def test_remove_valid_product(self):
        self.cart1.remove_from_cart(self.prod1.product_name)
        self.assertNotIn(self.prod1, self.cart1.cart_items)

    # def test_display_cart(self):
    #     self.cart1.add_to_cart(self.prod1)
    #     self.assertEqual(self.prod1, self.cart1.display_cart())

    def test_remove_invalid_product(self):
        self.cart1.add_to_cart(self.prod1)
        self.cart1.add_to_cart(self.prod2)
        self.assertEquals(
            self.cart1.remove_from_cart("Hat"), "Product doesn't exist in the cart\n"
        )
        print(self.cart1.remove_from_cart("Hat"))

    def test_display_empty_cart(self):
        self.assertEqual(self.cart1.display_cart(), "Cart is empty.\n")
