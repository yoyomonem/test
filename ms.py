import time
from random import randint
def tech(trigger):
    print("We are Microsoft. We make technology.")
def make(obj_c, see_if_is_found):
    answer = input("Objective-C is good. Do you want to make it? (Y/n) ")
    if answer == "Y" or answer == "y":
        print("Good choice. Let's get going to Make.")
        time.sleep(2)
        print("First, let's use the BSoD's physical memory dump.")
        time.sleep(2)
        print("Beginning dump of physical memory...")
        time.sleep(3)
        print("Physical memory dump complete.")
        print("Then we begin to \"Make\".")
        time.sleep(3)
    else:
        print("Abort.")
make("yes", "yes")
