from classes.Product import Product
from classes.PhyProduct import PhysicalProduct
from classes.DigiProduct import DigitalProduct
from classes.Supplier import Supplier

class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    @property
    def products(self)-> list[Product]:# to bypass privte attribute
        return self.__products
    
    def display_all(self)-> None:
        if not self.__products:
            print("Inventory is empty.")
            return
        
        for product in self.__products:
            if isinstance(product, PhysicalProduct):
                product.display_information()
                print("------------------------")
            elif isinstance(product, DigitalProduct):
                product.display_information()
                print("------------------------")


    def add_product(self, product: Product)-> None:
        self.__products.append(product)

    def remove_product(self, product_id:str):
        for product in self.__products:
            if product._Product__product_id == product_id:
                self.__products.remove(product)
                return True
        return False  

    def search_product(self, product_id:str):
        for product in self.__products:
            if product._Product__product_id == product_id:
                return product
        return None
    def to_list(self):
        return [product.to_dict() for product in self.__products]