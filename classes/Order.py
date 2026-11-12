from classes.Product import Product
from classes.Orderline import Orderline

class Order:
    def __init__(self, order_id: str):
        self.__order_id = order_id
        self.__orderlines : list[Orderline] = []

    def add_orderline(self, product: Product, quantity: int):
        orderline = Orderline(product, quantity)
        self.__orderlines.append(orderline)

    def calculate_total(self) -> float:
        total = 0.0
        for orderline in self.__orderlines:
            total += orderline.calculate_subtotal()
        return total

    def remove_orderline(self, product_id: str):
        for orderline in self.__orderlines:
            if orderline._Orderline__product._Product__product_id == product_id:
                self.__orderlines.remove(orderline)
                return True
        print(f"Orderline with product ID {product_id} not found.")