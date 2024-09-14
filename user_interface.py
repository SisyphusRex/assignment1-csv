#Walter Podewil
#CIS 226
#September 14, 2024
import typing
from typing import Union

class UserInterface:
    menu_list = [1, 2, 3, 4, 5]
    ##################
    # Constructor    #
    ##################
    def __init__(self, **kwargs):
        ...

    ##############
    # Methods    #
    ##############
    def display_menu(self):
        #displays menu, returns user choice with an int
        """Display Menu"""
        while check == True:
            user_input = input("Enter the number of your selection:\n"
                                "1. Load File\n"
                                "2. Print List\n"
                                "3. Search List\n"
                                "4. Add New Beverage\n"
                                "5. Exit")
            check, final_input = self.__check_menu_input(user_input)
        self.__evaluate_menu_input(final_input)

    def __check_menu_input(self, n: int) -> Union[bool, int]:
        """Evaluates user menu input"""
        #tries to cast input to int, catches exception then checks if it is a menu item
        try:
            x = int(n)
        except ValueError:
            print("Not an integer.")
            pass
        if n in self.menu_list:
            return False, x
        else:
            print("You must type 1, 2, 3, 4, or 5")
            return True, None

    def __evaluate_menu_input(self, n: int):
        """Move to user's choice"""
        match n:
            case 1:
                #load file
                ...
            case 2:
                #print list
                ...
            case 3:
                #search list
                ...
            case 4:
                #add new beverage
                ...
            case 5:
                #exit
                ...
