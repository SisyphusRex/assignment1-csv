#Walter Podewil
#CIS 226
#September 14, 2024

#System Imports
from typing import Union

#First Party Imports

#Third Party Imports


class Beverage:
    ####################
    # Constructor      #
    ####################
    def __init__(self, bId: str, name: str, pack: str, price: Union[float, int] ,
                 active: bool):
        """Constructor"""
        self.bId = bId
        self.name = name
        self.pack = pack
        self.price = price
        self.active = active

    ####################
    # Methods          #
    ####################
    def __str__(self) -> str:
        """String Method"""
        return (f"{self.bId:<6} {self.name:<50} {self.pack:<15} {self.__format_decimal(float(self.price)):<6} "
                f"{self.active:<5}")

    @property
    def __format_decimal(self, n: float) -> str:
        """Format Decimal"""
        return f"${n:.2f}"

class BeverageCollection:
    ################
    # Constructor  #
    ################
    def __init__(self, __beverages: list = None):
        """Constructor"""
        self.__beverages = __beverages or []

    #################
    # Methods       #
    #################
    def add(self, n: Beverage):
        """Add Beverage"""
        self.__beverages.append(n)


    def search(self, n: str) -> Union[bool, Beverage]:
        """This searches the collection by ID"""
        for item in self.__beverages:
            if item.bId == n:
                return item
        return None

    def __str__(self) -> str:
        """String Method"""
        my_str = "\n".join(map(str, self.__beverages))
        return my_str

    def create_csv_list(self) -> list:
        """Create List for saving to .csv"""
        my_list = []
        for item in self.__beverages:
            individual = [item.bId, item.name, item.pack, item.price, item.active]
            my_list.append(individual)
        return my_list
