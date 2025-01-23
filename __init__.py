import json
import products
from cart import dao
from products import Product

class Cart:
    def _init_(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])
s

def get_cart(username: str) -> list:
    """
    Retrieves the user's cart and returns the list of product objects.
    """
    # Fetch cart details for the user
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []

    # Initialize the list to hold product IDs
    product_ids = []
    for cart_detail in cart_details:
        try:
            # Parse contents safely using json.loads
            evaluated_contents = json.loads(cart_detail['contents'])
            product_ids.extend(evaluated_contents)
        except json.JSONDecodeError:
            print(f"Error decoding JSON for cart contents: {cart_detail['contents']}")
            continue

    # Fetch all products in a single call
    products_list = [products.get_product(pid) for pid in product_ids]
    return products_list


def add_to_cart(username: str, product_id: int):
    """
    Adds a product to the user's cart.
    """
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    """
    Removes a product from the user's cart.
    """
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    """
    Deletes the entire cart for the user.
    """
    dao.delete_cart(username)

