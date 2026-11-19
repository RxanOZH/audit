from classes.Product import Product

class Orderline:
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.__product = product
        self.__quantity = quantity

    def calculate_subtotal(self)->float:
        return self.__product._Product__price * self.__quantity
    