#Walter Podewil
#CIS 226
#September 14, 2024

#System Imports
import sys
import typing
from typing import Union
import csv

#First Party Imports
from beverage import *
from utils import CSVProcessor

#Third Party Imports

class UserInterface:
    menu_list = [1, 2, 3, 4, 5]
    ##################
    # Constructor    #
    ##################
    def __init__(self, initialized: bool = True):
        self.initialized = initialized

    ##############
    # Methods    #
    ##############
    def display_menu(self):
        #displays menu, returns user choice with an int
        """Display Menu"""
        check = True
        while check == True:
            user_input = input("Enter the number of your selection:\n"
                                "1. Load File\n"
                                "2. Print List\n"
                                "3. Search List\n"
                                "4. Add New Beverage\n"
                                "5. Exit\n")
            check, final_input = self.__check_menu_input(user_input)
        #self.__evaluate_menu_input(final_input)
        return final_input

    def __check_menu_input(self, n: str) -> Union[bool, int]:
        """Evaluates user menu input"""
        #tries to cast input to int, catches exception then checks if it is a menu item
        try:
            x = int(n)
        except ValueError:
            print("Not an integer.")
            return True, None
        if x in self.menu_list:
            return False, x
        else:
            print("You must type 1, 2, 3, 4, or 5")
            return True, None

    def __evaluate_menu_input(self, n: int):
        """Move to user's choice"""
        match n:
            case 1:
                #load file
                if self.loaded == False:
                    self.__load_file()
                    print("File Loaded.")

                else:
                    print("File already loaded.")

            case 2:
                #print list
                #print("case 2")
                if self.loaded == False:
                    print("File must be loaded.")
                else:
                    self.__print_list()
            case 3:
                #search list
                #print("case 3")
                if self.loaded == False:
                    print("File must be loaded.")
                else:
                    self.__search_list()
            case 4:
                #add new beverage
                #print("case 4")
                if self.loaded == False:
                    print("File must be loaded.")
                else:
                    self.__add_new_beverage()
            case 5:
                #exit
                #print("case 5")
                self.__exit()


    def __load_file(self):
        """Load .csv"""
        #use csvprocessor class for this
        new_csv = CSVProcessor()
        self.collection = new_csv.load_csv()
        #self.collection = new_csv.collection
        self.loaded = True
        #print(self.collection)




    def print_list(self, collection: BeverageCollection):
        """print beverage list"""
        #print("__print_list")
        print(collection)

    def search_list(self, collection: BeverageCollection):
        """search for beverage"""
        #print("__search_list")
        my_input = input("Enter beverage ID: ")
        found = collection.search(my_input)
        if found:
            print(found)
        else:
            print("ID not found.")

    def add_new_beverage(self, collection: BeverageCollection) -> str:
        """Add beverage to list"""
        #print("__add_new_beverage")
        check0 = True
        while check0:
            my_input = input("Enter new beverage ID: ")
            found = collection.search(my_input)
            if found:
                print("That ID exists already.")
                check0 = True
            else:
                check0 = False
        bev_id = my_input
        my_input = input("Enter a Beverage Name: ")
        bev_name = my_input
        my_input = input("Enter a beverage pack: ")
        bev_pack = my_input
        check1 = True
        while check1:
            my_input = input("Enter a beverage price: ")
            check1, bev_price = self.__check_bev_price(my_input)
        check2 = True
        while check2:
            my_input = input("Is the beverage active?\n"
                                "Type 1 for Active\n"
                                "Type 2 for Inactive")
            if my_input == "1":
                bev_active = True
                check2 = False
            if my_input == "2":
                bev_active = False
                check2 = False
        return bev_id, bev_name, bev_pack, bev_price, bev_active
        #new_beverage = Beverage(bev_id, bev_name, bev_pack, bev_price, bev_active)


    def exit(self):
        print("Goodbye.")

    #def __check_id_input(self, n: str) -> Union[bool, str]:
     #   for item in self.collection.__beverages:
     #       if n == item.bId:
     #           return False, item
     #   print("Beverage ID not found in list.")
      #  return True, None

    def __check_bev_price(self, n: str) -> Union[bool, str]:
        try:
            x = float(n)
        except ValueError:
            print("Price must be a number.")
            return True, None
        return False, f"{x:.2f}"

    def already_loaded(self):
        print("File already loaded.")

    def load_message(self):
        print("Initial Load Complete.")

    def must_load(self):
        print("File must be loaded first.")