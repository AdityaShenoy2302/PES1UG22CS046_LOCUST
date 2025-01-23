import json
from typing import List

from cart import dao
from products import Product, get_product


class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict):
        return Cart(
            data['id'],
            data['username'],
            [get_product(product_id) for product_id in json.loads(data['contents'])],
            data['cost']
        )


def get_cart(username: str) -> List[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    items = []
    for cart_detail in cart_details:
        contents = json.loads(cart_detail['contents'])  # Use JSON for safety instead of eval
        items.extend(contents)

    # Fetch all products in one go to reduce individual queries (if `get_product` supports batching)
    products_list = [get_product(product_id) for product_id in items]
    return products_list


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)
