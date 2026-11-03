from abc import ABC, abstractmethod
from classes.Canbeshipped import CanBeShipped
from classes.Product import Product

class PhysicalProduct(Product, CanBeShipped ):
    def __init__(self, product_id, product_name, product_price, product_inventory, weight):
        super().__init__(product_id, product_name, product_price, product_inventory)
        self.__weight = weight

    def display_information(self):
        super().display()
        print(f"Weight: {self.__weight} kg")
        print(f"the shipping cost is{self.calculate_shipping_cost()}")

    def get_fulfillment_info(self):
        print("This Product neeed to be Physically Shipped.")

    def to_dict(self):
        data = super().to_dict()
        data["type"]="physical"
        data["weight"]= self.__weight
        return data
    def calculate_shipping_cost(self):
        ship_cost=  self.__weight * 10
        return ship_cost