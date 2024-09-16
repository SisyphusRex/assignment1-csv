#Walter Podewil
#CIS 226
#September 14, 2024

#System Imports
import typing
from typing import Union
import csv
import sys
#First Party Imports
from beverage import *
#Third Party Imports

class CSVProcessor:
    ###############
    # Constructor #
    ###############
    def __init__(self,csv: str = "datafiles\\beverage_list.csv", loaded: bool = False):
        self.csv = csv
        self.loaded = loaded



    ###############
    # Methods     #
    ###############
    def load_csv(self, collection: BeverageCollection) -> BeverageCollection:
        """Loads CSV"""
        #print(self.csv)
        if self.loaded == False:
            try:
                with open(self.csv, newline = '') as file:
                    #my_collection = BeverageCollection()
                    reader = csv.reader(file)
                    for line in reader:
                        bId = line[0]
                        name = line[1]
                        pack = line[2]
                        price = line[3]
                        active = line[4]
                        new_beverage = Beverage(bId, name, pack, price, active)
                        collection.add(new_beverage)
                    #self.collection = my_collection


            except FileNotFoundError:
                sys.exit(".csv file not found.")
            self.loaded = True
            return collection
        else:
            return None


    def __str__(self):
        return f"{self.csv}"