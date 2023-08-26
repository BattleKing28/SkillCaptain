class Product:
    def __init__(self, prodcut_name, product_price, product_quantity):
        self.product_name = prodcut_name
        self.product_price = product_price
        self.product_quantity = product_quantity

    # @staticmethod
    def display_product_info(self):
        print(
            f"Name: {self.product_name}\n Price: {self.product_price}\n Quantity: {self.product_quantity}"
        )


products = []


def register_product():
    try:
        name = str(input("Enter your product name: "))
        price = float(input("Enter your product price: "))
        quantity = int(input("Enter your product quantity: "))
    except Exception as err:
        print(err)
        return

    new_product = Product(name, price, quantity)

    products.append(new_product)

    print("\n New product added successfully \n")

    new_product.display_product_info()


register_product()
