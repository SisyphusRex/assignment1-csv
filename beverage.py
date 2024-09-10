import typing
from decimal import Decimal
from typing import Union

class Beverage:
    def __init__(self, id: str, name: str, pack: str, price: Union[float, int] ,
                 active: bool):
        self.id = id
        self.name = name
        self.pack = pack
        self.price = Decimal(price)
        self.active = active

    def __str__(self):
        return (f"ID: {self.id}, Name: {self.name}, Pack: {self.pack}, Price: {self.price}, "
                f"Active: {self.active}")

class BeverageCollection:
    def __init__(self, __beverages = []):
        self.__beverages = __beverages

    def add(self, n: Beverage):
        self.__beverages.append(n)

    def search(self, n: Beverage):
        if n in self.__beverages:
            return True
        else:
            return False

    def __str__(self):
        my_str = "\n".join(map(str, self.__beverages))
        return my_str
