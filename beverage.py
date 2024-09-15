#Walter Podewil
#CIS 226
#September 14, 2024


import typing
#from decimal import Decimal
from typing import Union


class Beverage:
    ####################
    # Constructor      #
    ####################
    def __init__(self, bId: str, name: str, pack: str, price: Union[float, int] ,
                 active: bool):
        self.bId = bId
        self.name = name
        self.pack = pack
        self.price = price
        self.active = active

    ####################
    # Methods          #
    ####################
    def __str__(self) -> str:
        return (f"ID: {self.bId}, Name: {self.name}, Pack: {self.pack}, Price: {self.__format_decimal(float(self.price))}, "
                f"Active: {self.active}")

    def __format_decimal(self, n: float) -> str:
        return f"${n:.2f}"

class BeverageCollection:
    #This initialization avoids passing a mutable object, a list, as the default value
    def __init__(self, __beverages: list = None):
        self.__beverages = __beverages or []


    def add(self, n: Beverage):
        self.__beverages.append(n)


    def search(self, n: str) -> Union[bool, Beverage]:
        """This searches the collection by ID"""
        for item in self.__beverages:
            if item.bId == n:
                return item
        return None

    def __str__(self) -> str:
        my_str = "\n".join(map(str, self.__beverages))
        return my_str
