#Walter Podewil
#CIS 226
#September 14, 2024

#System Imports
from typing import Union

#First Party Imports
from beverage import *

#Third Party Imports

class UserInterface:
    """This class handles all UI"""

    """Universal Menu List"""
    MENU_LIST = [1, 2, 3, 4, 5, 6]
    ##################
    # Constructor    #
    ##################
    def __init__(self, initialized: bool = True):
        """Constructor"""
        #"initialized" is never used, but I did not know how to initialize the class without a parameter
        self.initialized = initialized

    ##############
    # Methods    #
    ##############
    def display_menu(self) -> int:
        #displays menu, returns user choice with an int
        """Display Menu"""
        check = True
        while check == True:
            user_input = input("Enter the number of your selection:\n"
                                "1. Load File\n"
                                "2. Print List\n"
                                "3. Search List\n"
                                "4. Add New Beverage\n"
                                "5. Save Modified File\n"
                                "6. Exit\n")
            check, final_input = self.__check_menu_input(user_input)
        return final_input

    def __check_menu_input(self, n: str) -> Union[bool, int]:
        """Evaluates user menu input"""
        #tries to cast input to int, catches exception then checks if it is a menu item
        try:
            x = int(n)
        except ValueError:
            print("**Not an integer.\n")
            return True, None
        if x in self.MENU_LIST:
            return False, x
        else:
            print("**You must type 1, 2, 3, 4, 5, or 6\n")
            return True, None

    def print_list(self, collection: BeverageCollection):
        """print beverage list"""
        print(collection)

    def search_list(self, collection: BeverageCollection):
        """search for beverage"""
        my_input = input("Enter beverage ID: ")
        found = collection.search(my_input)
        if found:
            print(found)
        else:
            print("**ID not found.\n")

    def add_new_beverage(self, collection: BeverageCollection) -> str:
        """Add beverage to list"""
        check0 = True
        while check0:
            my_input = input("Enter new beverage ID: ")
            found = collection.search(my_input)
            if found:
                print("**That ID exists already.\n")
                check0 = True
            else:
                if len(my_input) <= 5:
                    check0 = False
                else:
                    print("**Beverage ID must be 5 characters or less.\n")
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


    def exit(self):
        """Says goodbye."""
        print("Goodbye.")

    def __check_bev_price(self, n: str) -> Union[bool, str]:
        """Checks input to beverage price"""
        try:
            x = float(n)
        except ValueError:
            print("**Price must be a number.\n")
            return True, None
        return False, f"{x:.2f}"

    def already_loaded(self):
        """Says already loaded"""
        print("**File already loaded.\n")

    def load_message(self):
        """Says load complete"""
        print("*Initial Load Complete.\n")

    def must_load(self):
        """Says file must be loaded """
        print("**File must be loaded first.\n")

    def file_saved(self):
        """Says file saved"""
        print("*File Saved.\n")
