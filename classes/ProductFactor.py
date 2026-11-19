from classes.Product import Product
from classes.PhyProduct import PhysicalProduct
from classes.DigiProduct import DigitalProduct
from classes.Supplier import Supplier


class ProductFactory:
    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Supplier,
        extra_info: float = 1.0
    ) -> Product:
        p_type = product_type.strip().lower()
        if p_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, extra_info, supplier)
        elif p_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, extra_info, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")