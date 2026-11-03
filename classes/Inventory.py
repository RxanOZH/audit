"""
_____________________________________
Inventory                            |   <-- Class Name
_____________________________________|   
- __products: list[Products]         |   <-- Attributes
_____________________________________|
+ display_all()                      |
+ add_product(product)               |   <-- Methods
+ search_product(product_id: str)    |
+ to_list(): list[dict]              |
_____________________________________|
"""

class Inventory:
    def __init__(self):
        self.__products = []

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return
        
        for product in self.__products:
            product.display()

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product._Product__product_id == product_id:
                return product
        return None
    def to_list(self):
        return [product.to_dict() for product in self.__products]