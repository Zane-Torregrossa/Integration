# Zane M Torregrossa
# This is Adventuria! A fun and diverse dungeon exploring game.
# Can you make it to the end alive?


# Starting Adventure
def start_adventure():
    print("You awake in a cold and dark room.")
    print("You see a red door on the right and a blue door to your left.")
    main_room()


# Creating a Beginning Room
def main_room():
    print("It seems you cannot see anything else in the room.")
    print("Do you pick the red door or the blue door?")
    main_room_doors = input(">")
    if main_room_doors in ["red door", "red", "right"]:
        print("You chose the red door. You begin to open the door...")
        red_door_room()
    elif main_room_doors in ["blue door", "blue", "left"]:
        print("You chose the blue door. You begin to open the door...")
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer.")
        main_room()


# Setting up Red Door Room
def red_door_room():
    print("You enter the room behind the red door.")
    print("There you see a great red dragon sleeping in the middle of the room.")
    print("Do you flee, fight, or sneak past it?")
    next_move = input(">")
    if "flee" in next_move:
        print("You turn around and go back the way you came.")
        main_room()
    elif "fight" in next_move:
        print("The dragon awakes and eats you whole. Well, that was tasty!")
        game_over()
    elif "sneak" in next_move:
        print("You begin to step past the dragon.")
        print("As you tippy-toe to the other side, you accidently step on the dragon's tail!")
        print("The dragon awakes and eats you whole. Well, that was tasty!")
        game_over()
    else:
        print("Sorry, it's either 'flee', 'fight' or 'sneak' as the answer.")
        red_door_room()


# Setting up Blue Door Room
def blue_door_room():
    print("You enter the room behind the blue door.")
    print("You glance around the room.")
    print("You can see a wooden chest on the left, a sleeping guard on the right, and a yellow door in the middle.")
    action_step1()


# Setting up Yellow Door Room
def yellow_door_room():
    print("After unlocking the old, ancient door, you push it wide open; entering a room full of darkness.")
    print("There seems to be torches along the wall. Perhaps one can be sparked for a source of light?")
    print("Do you want to light a torch?")
    choice_step3()


# Setting up Action Commands
def action_step1():
    print("What do you want to do?")
    action_step1 = input(">")
    if action_step1.lower() in ["wooden", "chest", "left"]:
        print("You reach for the wooden chest. Are you sure you want to open it?")
        choice_step1()
    elif action_step1 in ["yellow", "middle", "door"]:
        print("You jiggle the door handle, but it won't open!")
        action_step2()
    elif action_step1 in ["guard", "right"]:
        print("You turn to face the guard.")
        action_step3()
    else:
        print("Sorry, it's either 'chest', 'yellow', or 'guard' as the answer.")
        blue_door_room()


def action_step2():
    print("Do you want to check the guard, the yellow door, or go back to previous room?")
    action_step2 = input(">")
    if action_step2 in ["go back", "previous room"]:
        main_room()
    elif action_step2 in ["yellow", "middle", "door"]:
        print("You jiggle the door handle, but it won't open!")
        blue_door_room()
    elif action_step2 in ["guard", "right"]:
        print("You turn to face the guard.")
        action_step3()
    else:
        print("Sorry, your choices are 'go back', 'yellow', or 'guard'.")
        blue_door_room()


def action_step3():
    print("The guard is still sleeping. Would you like to pickpocket, fight, or leave him be?")
    action_step3 = input(">")
    if action_step3 == "pickpocket":
        print("You begin going through his pockets...")
        print("You find a key with a skull on it.")
    elif action_step3 == "fight":
        print("You go to attack the guard, but he swiftly dodges your attack!")
    elif action_step3 == "leave":
        print("Well okay then, let the man sleep in peace.")
        action_step2()
    else:
        print("Sorry, your choices are 'pickpocket', 'fight', or 'leave'.")
        blue_door_room()


# Setting up Choice Commands
def choice_step1():
    treasure_chest = ["Diamonds", "Gold", "Silver", "Sword"]
    choice_step1 = input(">")
    if choice_step1 == "yes":
        print("Let's see what's in here...")
        print("The chest creaks open. You can hear the guard is still sleeping. That's one heavy sleeper!")
        print("Inside the chest, you find:")
        for treasure in treasure_chest:
            print(treasure)
            print("There is a warning inside the chest!")
            print("Adventurer, this is a magical chest. You get one item, the rest will disappear! Choose carefully...")
            print("Which item will you take?")
            choice_step2()
    elif choice_step1 == "no":
        print("Oh okay, no loot for you.")
        action_step2()
    else:
        print("Sorry, your choices are 'yes' or 'no'.")
        blue_door_room()


def choice_step2():
    choice_step2 = input(">")
    if choice_step2 == "Diamonds":
        print("You chose Diamonds. Oh how they sparkle!")
        action_step2()
    elif choice_step2 == "Gold":
        print("You chose Gold. Is there ever enough wealth?")
        action_step2()
    elif choice_step2 == "Silver":
        print("You chose Silver. What are you? Stupid or something?")
        action_step2()
    elif choice_step2 == "Sword":
        print("You chose Sword. Ah, what a fine weapon you have there!")
        action_step2()
    else:
        print("Sorry, your choices are 'Diamonds', 'Gold', 'Silver', or 'Sword'.")
        blue_door_room()


def choice_step3():
    choice_step3 = input(">")
    if choice_step3 == "yes":
        print("The torch lights. A light is now provided.")
    elif choice_step3 == "no":
        print("You fool, how will you see in this darkness?")
    else:
        print("Sorry, your choices are 'yes' or 'no'.")
        yellow_door_room()

# Setting up Player and Begins Game
def main():
    player_name = input("What is your name, Adventurer? >")
    print("Your name is {}.".format(player_name))
    start_adventure()


# Resets the Game or Quit
def game_over():
    reset_game = input("Game Over, Adventurer. Try again? 'yes' or 'no' >")
    if "yes" in reset_game:
        start_adventure()
    elif "no" in reset_game:
        print("Pity. We thought you were the Chosen One.")
        quit()


if __name__ == '__main__':
    main()
