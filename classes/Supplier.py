from abc import ABC, abstractmethod

class Supplier():
    def __init__(self, supplier_id: str, supplier_name: str, supplier_email: str):
        self.__supplier_id = supplier_id
        self.__name = supplier_name
        self.__email = supplier_email

    def display(self)-> None:
        print(f"ID: {self.__supplier_id}|Name: {self.__name}|Email: {self.__email}")

    def to_dict(self)-> dict:
        return {
            "supplier_id": self.__supplier_id,
            "name": self.__name,
            "email": self.__email
        }
