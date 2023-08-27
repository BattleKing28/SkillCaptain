class Product:
    def __init__(self, prodcut_name, product_price, product_quantity):
        self.product_name = prodcut_name
        self.product_price = product_price
        self.product_quantity = product_quantity

    def display_product_info(self):
        print(
            f"Name: {self.product_name}\n Price: {self.product_price}\n Quantity: {self.product_quantity}\n"
        )


class Cart:
    def __init__(self, user_name):
        self.user_name = user_name
        self.cart_items = []

    def add_to_cart(self, product):
        if not product:
            print("Cannot add empty product")
            return
        self.cart_items.append(product)
        print(f"{product.product_name} added to cart\n")

    def remove_from_cart(self, product_name):
        for item in self.cart_items:
            if item.product_name == product_name:
                self.cart_items.remove(item)
                print(f"{product_name} removed from cart\n")
                return
        print("Product doesn't exist in the cart\n")
        return "Product doesn't exist in the cart\n"

    def display_cart(self):
        print(f"Cart items for user: {self.user_name}")
        if not self.cart_items:
            print("Cart is empty.\n")
            return "Cart is empty.\n"
        else:
            for item in self.cart_items:
                item.display_product_info()


prod1 = Product("Tshirt", 50, 2)
prod2 = Product("Bat", 500, 10)

cart1 = Cart("John")

cart1.add_to_cart(prod1)
cart1.add_to_cart(prod2)

cart1.display_cart()

cart1.remove_from_cart("t")

cart1.display_cart()
