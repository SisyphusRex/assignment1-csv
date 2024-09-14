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
    def __init__(self, csv = "datafiles\\beverage_list.csv", collection = None):
        self.csv = csv
        self.collection = collection

    ###############
    # Methods     #
    ###############
    def load_csv(self):
        """Loads CSV"""
        try:
            with open(self.csv) as file:
                my_collection = BeverageCollection()
                reader = csv.reader(file)
                for line in reader:
                    bId, name, pack, price, active = line.split(",")
                    new_beverage = Beverage(bId, name, pack, price, active)
                    my_collection.add(new_beverage)


        except FileNotFoundError:
            sys.exit(".csv file not found.")

        self.collection = my_collection