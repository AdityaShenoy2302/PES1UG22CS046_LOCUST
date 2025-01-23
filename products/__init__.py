from typing import List
from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict):
        return Product(
            data['id'],
            data['name'],
            data['description'],
            data['cost'],
            data['qty']
        )


def list_products() -> List[Product]:
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with ID {product_id} does not exist")
    return Product.load(product_data)


def add_product(product: dict):
    if not all(key in product for key in ('id', 'name', 'description', 'cost', 'qty')):
        raise ValueError("Product data is incomplete")
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
