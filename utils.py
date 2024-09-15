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
    def __init__(self, csv = "datafiles\\beverage_list.csv", collection: BeverageCollection = None):
        self.csv = csv
        self.collection = collection

    ###############
    # Methods     #
    ###############
    def load_csv(self) -> BeverageCollection:
        """Loads CSV"""
        #print(self.csv)
        try:
            with open(self.csv, newline = '') as file:
                my_collection = BeverageCollection()
                reader = csv.reader(file)
                for line in reader:
                    bId = line[0]
                    name = line[1]
                    pack = line[2]
                    price = line[3]
                    active = line[4]
                    new_beverage = Beverage(bId, name, pack, price, active)
                    my_collection.add(new_beverage)
                    #self.collection = my_collection


        except FileNotFoundError:
            sys.exit(".csv file not found.")
        return my_collection


    def __str__(self):
        return f"{self.csv}"