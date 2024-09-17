#Walter Podewil
#CIS 226
#September 14, 2024

#System Imports
import csv
import sys
import os
import pathlib

#First Party Imports
from beverage import *
#Third Party Imports

class CSVProcessor:
    ###############
    # Constructor #
    ###############
    def __init__(self,csv: str = "datafiles\\beverage_list.csv", loaded: bool = False):
        """Constructor"""
        self.csv = csv
        self.loaded = loaded



    ###############
    # Methods     #
    ###############
    def load_csv(self, collection: BeverageCollection) -> BeverageCollection:
        """Loads CSV"""
        if self.loaded == False:
            try:
                with open(self.csv, newline = '') as file:
                    reader = csv.reader(file)
                    for line in reader:
                        bId = line[0]
                        name = line[1]
                        pack = line[2]
                        price = line[3]
                        active = line[4]
                        new_beverage = Beverage(bId, name, pack, price, active)
                        collection.add(new_beverage)



            except FileNotFoundError:
                sys.exit(".csv file not found.")
            self.loaded = True
            return collection
        else:
            return None

    def save_csv(self, beverage_list: list):
        """Saves modified csv"""
        with open("datafiles\modified_beverage_list.csv", "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(beverage_list)

    def __str__(self) -> str:
        """String method"""
        return f"{self.csv}"

    def __find_files(self, directory: str = "datafiles") -> list:
        """Creates list of .csv files in datafiles"""
        my_files = list(pathlib.Path(directory).glob("*.csv"))
        return my_files
