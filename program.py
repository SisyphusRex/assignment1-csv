#Walter Podewil
#CIS 226
#September 15, 2024

#System Imports

#First Party Imports
from user_interface import *
#Third Party Imports



"""Program code"""

def main(*args):
    """Method to run program"""
    new_interface = UserInterface()
    running = True
    while running:
        new_interface.display_menu()
