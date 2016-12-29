import time
import random

def theRoad():
    print("\nYou are now standing in front of your family's ancient castle...")
    print("You breathe deep the fragrance of the outdoors...the wood, the earth, the plants...the adventure!")
    print("And so begins the adventure of...")
    time.sleep(3)
    print("\nThe quest for the crescent stone!")
    time.sleep(5)
    print("\nYou peer out and see 2 directions to travel...the well worn path the east leads to the 'Deserted Cave'.")
    print("The western path has grown over and you are not sure where it may take you...beginners should choose east")
    time.sleep(2)
    print("Which path will you choose,'e' or 'w'...")
    direction = input("\n-> ")
    if direction == "e":
        print("You head east...")
        time.sleep(3)
        desertedCave()
    elif direction == "w":
        print("You head west...")
        time.sleep(3)
        unknownRoad()
