from abc import ABC, abstractmethod
from classes.Product import Product
from classes.Supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id, product_name, product_price, product_inventory, file_size, supplier):
        super().__init__(product_id, product_name, product_price, product_inventory, supplier)
        self.__file_size: float = file_size

    def display_information(self)-> None:
        super().display()
        print(f"File Size: {self.__file_size} MB")
        self._supplier.display()  # Assuming Supplier class has a display method

    def get_fulfillment_info(self)-> None:
        print("This product needs to be Downloaded digitally.")

    def to_dict(self)-> dict:
            data = super().to_dict()
            data["type"]="digital"
            data["file_size"]= self.__file_size
            data["supplier"] = self._supplier.to_dict()  # Assuming Supplier class has a to_dict method
            return data