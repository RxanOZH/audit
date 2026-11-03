from .Product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, product_name, product_price, product_inventory, file_size):
        super().__init__(product_id, product_name, product_price, product_inventory)
        self.__file_size = file_size

    def display_information(self):
        super().display()
        print(f"File Size: {self.__file_size} MB")

    def get_fulfillment_info(self):
        print("This product needs to be Downloaded digitally.")

    def to_dict(self):
            data = super().to_dict()
            data["type"]="digital"
            data["file_size"]= self.__file_size
            return data