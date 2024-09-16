
#Walter Podewil
#CIS 226
#September 15, 2024

#System Imports

#First Party Imports
from user_interface import *
from beverage import *
from utils import *
#Third Party Imports



"""Program code"""


def main(*args):
    """Method to run program"""
    my_interface = UserInterface()
    my_utils = CSVProcessor()
    my_collection = BeverageCollection()
    running = True
    while running:
        choice = my_interface.display_menu()
        match choice:
            case 1:
                """Load .csv to BeverageCollection"""
                my_collection = my_utils.load_csv(my_collection)
                my_interface.load_message()
            case 2:
                """Print List"""
                if my_utils.loaded:
                    my_interface.print_list(my_collection)
                else:
                    my_interface.must_load()
            case 3:
                """Search List"""
                if my_utils.loaded:
                    my_interface.search_list(my_collection)
                else:
                    my_interface.must_load()
            case 4:
                """Add New Beverage to List"""
                if my_utils.loaded:
                    my_id, my_name, my_pack, my_price, my_active = my_interface.add_new_beverage(my_collection)
                    new_beverage = Beverage(my_id, my_name, my_pack, my_price, my_active)
                    my_collection.add(new_beverage)
                else:
                    my_interface.must_load()
            case 5:
                """Save Modified File"""
                if my_utils.loaded:
                    my_utils.save_csv(my_collection)
            case 6:
                """Exit"""
                my_interface.exit()
                sys.exit()

