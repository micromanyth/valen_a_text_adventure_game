import time
from playerClass import player
from theRoad import theRoad

def mainHall():
    print("\nYou are standing in the great marble hall of your family's castle.")
    print("there is a large fire pit smouldering in the center of the room.")
    print("Several servants are shuffling about working on various tasks.")
    time.sleep(3)
    print("\nYou see 4 exits in this room. To the north is the armoury, the east a training room.")
    print("The west houses the grand library. If you choose south you will leave the castle and be")
    print("on the road. Choices are ('n', 's', 'e', 'w', or 'q' to quit)")
    time.sleep(1)
    move = input("-> ")

    if move == "n":
        armoury()
    elif move == "e":
        trainingRoom()
    elif move == "w":
        library()
    elif move == "s":
        theRoad()
    elif move == "q":
        quit()
    else:
        mainHall()

def armoury():
    print("Shadows flicker on the wall and the ringing of hammer on steel sings in your ears")
    print("as you enter the armoury.")
    time.sleep(2)
    print("\nA stout dwarf lifts his gaze from the iron anvil and watches as you enter. He wipes his brow")
    print("on the sleeve of his tunic and coughs once before saying \n'Hello my lord! How may I assist you?'")
    time.sleep(2)
    option = input("\nType '$' to shop or 's' to return to the Hall ->  ")
    if option == "$":
        shop()
    elif option == "s":
        mainHall()

def shop():
    print("An oil lamp lights up the wooden counter where a very old woman with raven hair tends the shop.")
    print("'Hello, my lord. What can I get for you today?'")
    time.sleep(3)
    shopItems = ["Bronze Axe", "Steel Long Sword", "Glaive"]

    print("Three weapons lay on the counter,")
    print(shopItems)
    time.sleep(2)
    choice = input("Each item has an attack value of 5, select the axe with '1', the sword '2', or the glaive '3': ")
    time.sleep(2)
    if choice == "1":
        player.weapon = shopItems[1]
        print("You now wield the Bronze Axe. You thank the shop keeper and head for the main hall...")
        time.sleep(3)
    elif choice == "2":
        player.weapon = shopItems[2]
        print("You now wield the Steel Long Sword. You thank the shop keeper and head for the main hall...")
        time.sleep(3)
    elif choice == "3":
        player.weapon = shopItems[3]
        print("You now wield the Glaive. You thank the shop keeper and head for the main hall...")
        time.sleep(3)
    else:
        print("That is not a valid selection, please enter 1,2,or 3...")
        time.sleep(2)
        shop()
    mainHall()

def trainingRoom():
    print("\nAn old grizzled commander barks out orders as young acolytes swing weapons into lifeless training ")
    print("dummies.")
    print("He turns and spits into a crusty spatoon leaning against the weapon-lined wall.")
    print("'You need training young master?'")
    print("His eyes twinkle as he awaits your answer.")
    time.sleep(2)
    option = input("\nType 'T' to practice your weapon skills or 'w' to return to the Hall ->  ")
    time.sleep(1)
    if option == "T":
        print("\nThe commander shoves you in front of a sad old training dummy. 'Swing, Parry, Thrust! HAHAHA' he ")
        print("shouts in your ears")
        print("\nYou thrust your weapon into the dummy and watch as it spins in return, flinging it's wooden arms ")
        print("wildly about")
        print("You spin bringing your weapon crashing down onto it's featureless face. The dummy seems bored...")
        time.sleep(5)
        print("\n'HAHA!' Nice work lad. Now you watch yourself out on the road...Heard tale of many a foul creatures ")
        print("lurking about as of late.")
        time.sleep(2)
        print("\nYou turn and leave the room, and head back into the great Hall")
        print("\n")
        time.sleep(4)
        mainHall()
    elif option == "w":
        mainHall()

def library():
    print("\nThe rich odor of old volumes of text fills your nose as you cross into the enormous library.")
    print("Your eyes scan the spines of the books lining the tall shelves that span over several levels.")
    print("You recall,for a moment, the memories of grand adventure and great longing to see the world")
    print("after reading through these wonderful stories.")
    time.sleep(2)
    print("The young librarian lifts her gaze from an old manuscript and gives you a smile.")
    print("'My lord! How may I assist you today?' she says and pulls her glasses from her face")
    option = input("\nYou may examine the Adventurer's Tome by typing 'A' or exit to the hall with 'e'-> ")
    if option == "A":
        print("You kindly ask of the librarian to fetch you the Adventurer's Tome.")
        print("She smiles, sensing your desire for adventure, and brings the novel to you")
        adventureTome()
        mainHall()
    elif option == "e":
        mainHall()

def adventureTome():
    print("\nYou turn the heavy cover open and begin to scan the pages...")
    print("'...the first rule of King Straff was a long and celebrated peaceful time.'")
    print("'King Straff's most trusted advisor, the great wizard Vermulti, kept watch'")
    print("'over the crescent stone. A powerful and sacred object with magnificent magical'")
    print("'capabilities. Alas, the stone was stolen by the dark prince, Mats'")
    time.sleep(4)
    print("You pull your eyes from the tome, recalling the enormous tapestry depciting the")
    print("crescent stone in the great hall. It's majesty left an impression on your young mind.")
    time.sleep(5)
    print("\nYour eyes return to the pages...")
    print("'Mats created an army of the dead and plunged the world into a violent chaos.'")
    print("'His reign over Valen has taken many. The world has fallen to a plight. A darkness deep.'")
    print("'Upon Straff's death bed, as his life quickened with age, he spoke finally...'")
    print("'The time has come for a new warrior to challenge Mats and reclaim the crescent stone...'")
    time.sleep(10)
    print("You pull your eyes up from the book. You know your purpose. Your passion. ")
    print("You must seek the crescent stone...")
    time.sleep(5)
    print("With a fire surging in your veins you turn and head back to the great hall...")
    time.sleep(3)
    print("\n")
    mainHall()

