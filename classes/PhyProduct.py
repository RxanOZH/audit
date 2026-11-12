from abc import ABC, abstractmethod
from classes.Canbeshipped import CanBeShipped
from classes.Product import Product
from classes.Supplier import Supplier

class PhysicalProduct(Product, CanBeShipped ):
    def __init__(self, product_id: str, product_name: str, product_price: float, product_inventory: int, weight: float, supplier: Supplier):
        super().__init__(product_id, product_name, product_price, product_inventory, supplier)
        self.__weight: float = weight

    def display_information(self)-> None:
        super().display()
        print(f"Weight: {self.__weight} kg")
        print(f"the shipping cost is {self.calculate_shipping_cost()}")
        self._supplier.display()  # Assuming Supplier class has a display method

    def get_fulfillment_info(self)-> None:
        print("This Product neeed to be Physically Shipped.")

    def calculate_shipping_cost(self)-> float:
        ship_cost=  self.__weight * 10
        return ship_cost

    def to_dict(self)-> dict:
        data = super().to_dict()
        data["type"]="physical"
        data["weight"]= self.__weight
        data["supplier"] = self._supplier.to_dict()  # Assuming Supplier class has a to_dict method
        return data
    