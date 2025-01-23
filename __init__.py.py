from products import dao


class Product:
    def _init_(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict):
        """
        Creates a Product instance from a dictionary.
        """
        return Product(
            data['id'], 
            data['name'], 
            data['description'], 
            data['cost'], 
            data.get('qty', 0)  # Default quantity to 0 if not provided
        )


def list_products() -> list[Product]:
    """
    Returns a list of all products as Product objects.
    """
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """
    Fetches a product by its ID and returns it as a Product object.
    """
    product_data = dao.get_product(product_id)
    return Product.load(product_data)


def add_product(product: dict):
    """
    Adds a new product to the database.
    """
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """
    Updates the quantity of a product. Quantity must be non-negative.
    """
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
