"""
_____________________________________
Product                              |   <-- Class Name
_____________________________________|
- __product_id: String               |    
- __name: String                     |   <-- Attributes
- __price: float                     |
- __stock: int                       |
_____________________________________|            |
+ update_stock(quantity : int): void |   <-- Methods
+ display(): void        |
+ to_dict(): dict                    |
_____________________________________|
"""
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, product_name, product_price, product_inventory):
        self.__product_id = product_id
        self.__name = product_name
        self.__price = product_price
        self.__stock = product_inventory

    def display(self):
        print(f"ID: {self.__product_id}|Name: {self.__name}|Price: {self.__price}|Stocks: {self.__stock}")

    def update_stock(self, new_stock):
        self.__stock = new_stock

    
    def get_fulfillment_info(self):
        pass

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }