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
from classes.Supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, product_name: str, product_price: float, product_inventory: int, supplier: Supplier = Supplier):
        self.__product_id = product_id
        self.__name = product_name
        self.__price = product_price
        self.__stock = product_inventory
        self._supplier = supplier

    def display(self)-> None:
        print(f"ID: {self.__product_id}|Name: {self.__name}|Price: {self.__price}|Stocks: {self.__stock}")
        

    def update_stock(self, new_stock: int):
        self.__stock = new_stock

    
    def get_fulfillment_info(self)-> None:
        pass

    def to_dict(self)-> dict:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }