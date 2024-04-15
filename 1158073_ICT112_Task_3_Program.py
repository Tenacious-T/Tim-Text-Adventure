# This file is a "multi madness text game" created for ICT112 task 3 
# Created 16/06/2023 by Timothy Szoke


# Imported module 
import os

# File setup and secondary functions
def file_setup():
    """Creates a default room setup file and a default item setup file"""
    default_rooms = [
        {
            "room": "foyer",
            "description": "a large ornate entrance hall. The hall has a "
                            "locked ornate door.",
            "north": "nothing",
            "south": "nothing",
            "east": "dining room",
            "west": "living room",
            "escape room": "yes"
        },
        {
            "room": "dining room",
            "description": "a large mostly empty room dominated by a large "
                           "wooden table stacked with empty baked bean cans "
                           "surrounded by chairs",
            "north": "nothing",
            "south": "nothing",
            "east": "pantry",
            "west": "foyer",
            "escape room": "no"
        },
        {
            "room": "pantry",
            "description": "a small room with stacks of canned foods and "
                           "various seasonings",
            "north": "nothing",
            "south": "nothing",
            "east": "nothing",
            "west": "dining room",
            "escape room": "no"
        },
        {
            "room": "living room",
            "description": "a comfortable room with a comfortable lounge",
            "north": "bathroom",
            "south": "nothing",
            "east": "foyer",
            "west": "nothing",
            "escape room": "no"
        },
        {
            "room": "bathroom",
            "description": "a white tiled bathroom with an ever dripping "
                           "sink tap",
            "north": "nothing",
            "south": "living room",
            "east": "nothing",
            "west": "nothing",
            "escape room": "no"
        }
    ]
    with open("room_setup.txt", "w") as file:
        for room in default_rooms:
            room_data = [
                room["room"],
                room["description"],
                room["north"],
                room["south"],
                room["east"],
                room["west"],
                room["escape room"]
            ]
            formatted_line = "|".join(room_data) + "\n"
            file.write(formatted_line)
    default_items = [
        {
            "item": "broken rotary telephone",
            "item description": "an old rotary phone, it doesn't seem able "
                                "to rotate anymore",
            "item hint": "not everything has a use, sometimes a broken "
                         "rotary phone is just a broken rotary phone",
            "item location": "foyer",
            "escape item": "no"
        },
        {
            "item": "can of baked beans",
            "item description": "a can of baked beans that "
                                "rattles when shaken",
            "item hint": "whatever is in the can doesn't seem like baked "
                         "beans",
            "item location": "pantry",
            "escape item": "no"
        },
        {
            "item": "can of pineapples",
            "item description": "a seemingly normal can of sliced pineapples",
            "item hint": "there sure are a lot of cans, are any different?",
            "item location": "pantry",
            "escape item": "no"
        },
        {
            "item": "can of corn kernels",
            "item description": "a seemingly normal can of corn kernels",
            "item hint": "there sure are a lot of cans, are any different?",
            "item location": "pantry",
            "escape item": "no"
        },
        {
            "item": "cassette tape",
            "item description": "a casset table on which someone has written "
                                "\"I love baked beans!\"",
            "item hint": "whatever is recorded on the tape is likely "
                         "about baked beans",
            "item location": "bathroom",
            "escape item": "no"
        },
        {
            "item": "rusty can opener",
            "item description": "This can opener has seen better days",
            "item hint": "if I could find a can, I might be able to open it",
            "item location": "living room",
            "escape item": "no"
        },
        {
            "item": "plunger",
            "item description": "a wooden plunger with a red suction cup",
            "item hint": "This would be just what I needed if what I needed "
                         "was to unclog something",
            "item location": "bathroom",
            "escape item": "no"
        }            
    ]
    with open("item_setup.txt", "w") as file:
        for item in default_items:
            item_data = [
                item["item"],
                item["item description"],
                item["item hint"],
                item["item location"],
                item["escape item"]
            ]
            formatted_line = "|".join(item_data) + "\n"
            file.write(formatted_line)

def read_setup_files():
    """Reads and combines and item and room setup files and returns the data
    as a list of dictionaries containing room and item information."""
    rooms = []
    items = []
    with open("room_setup.txt", "r") as room_file:
        for line in room_file:
            room_data = line.strip().split("|")
            room = {
                "room": room_data[0],
                "description": room_data[1],
                "north": room_data[2],
                "south": room_data[3],
                "east": room_data[4],
                "west": room_data[5],
                "escape room": room_data[6],
                "items": []
            }
            rooms.append(room)
    with open("item_setup.txt", "r") as item_file:
        for line in item_file:
            item_data = line.strip().split("|")
            item = {
                "item": item_data[0],
                "description": item_data[1],
                "hint": item_data[2],
                "location": item_data[3],
                "escape item": item_data[4]
            }
            items.append(item)
    for room in rooms:
        for item in items:
            if item['location'] == room['room']:
                room['items'].append(item)
    return rooms

def player_profile():
    """Creats or selects a player profile to use in the game"""
    print(" PROFILE SELECTION ".center(40,"*"))
    profile_dict = {}
    if not os.path.isfile("player_profiles.txt"):
        profile_yes_no = ""
        while profile_yes_no != "y":
                profile_input = input("No player profiles found, please "
                                      "enter the username for a new "
                                      "profile\n")
                print("is \""+ profile_input + "\" what you want the profile "
                      "to be called?\n")
                profile_yes_no = yes_or_no()
                if profile_yes_no == "y":
                    with open("player_profiles.txt", "w") as file:
                        #name, wallet total, best score (lowest score)
                        file.write(profile_input +"|100|0\n")
                    profile_dict = {"username": profile_input,
                                    "wallet total": 100,
                                    "best score": 0}
                    return profile_dict
    print("Existing profiles:")            
    with open("player_profiles.txt", "r") as file:
        count = 0
        for line in file:
            count += 1
            profile_data = line.strip().split("|")
            print(str(count)+": " +profile_data[0]) 
    profile_choice = 0
    while profile_choice not in range(1, count+2):
        try:
            profile_choice = int(input("Please enter the number of the "
                                "profile to select it, or enter "
                                +str(count+1)+" to create a new profile\n"))
        except:
            print("invalid user input\n")    
    if profile_choice in range(1, count+1):
        with open("player_profiles.txt", "r") as file:
            count = 0
            for line in file:
                count += 1
                profile_data = line.strip().split("|")
                profile_dict = {
                "username": profile_data[0],
                "wallet total": int(profile_data[1]),
                "best score": int(profile_data[2])
                }
                if count == profile_choice:
                    return profile_dict
    if profile_choice == count + 1:  
        with open("player_profiles.txt", "a") as file:
            profile_yes_no = ""
            while profile_yes_no != "y":
                profile_input = input("please enter the username for a "
                                      "new profile\n")
                print("is \""+ profile_input + "\" what you want the " 
                        "profile to be called?\n")
                profile_yes_no = yes_or_no()
                if profile_yes_no == "y":
                    with open("player_profiles.txt", "a") as file:
                        #name, wallet total, best score (lowest score)
                        file.write(profile_input +"|100|0|\n")
                        profile_dict = {"username": profile_input,
                                        "wallet total": 100,
                                        "best score": 0}
                        return profile_dict


# Primary game functions
def tutorial():
    """Provides the user with a tutorial of the game and valid inputs"""
    print(" TUTORIAL ".center(40,"*"))
    print("The goal of the game is to find a way to escape the weird house "
          "you find yourself in. This can be accomplished by finding the "
          "appropriate item and using that item in the correct room.\n"
          "\nPlayers should aim to complete the game as fast as possible. " 
          "Every action the user takes during the game, aside from " 
          "\"Tutorial\" or \"Quit\", will raise the player's score. "
          "Ultimately, the goal is to complete the game with the lowest " 
          "score.\n\nPlayers must also pay with their wallet when picking up "
          "items. A player's wallet is tied to their profile and persistent "
          "between games. A player's profile starts with $100, picking up an "
          "item costs $10. However, if an item is dropped without being used "
          "players will receive $5 back. Additionally, if a player has less "
          "than $20 in their wallet at the game start, players will be given "
          "enough cash to reach $20.\n")
    print(" USER ACTIONS ".center(40,"*"))
    print("By entering the following commands, players can perform actions:\n"
          "\n\"move (direction)\"\n"
          "Players may move North, South, East, or West. A correct command "
          "would be \"Move North\".\n"
          "\n\"Take (Item)\"\n"
          "Players my hold items they find, up to a maximum of three, by "
          "inputting take and the desired item. A correct command would be "
          "\"Take Radio\".\n"
          "\n\"Drop (item)\"\n"
          "Players may also any items they are holding in their inventory. A "
          "correct command would be \"Drop Radio\"\n"
          "\n\"Use (item)\" or \"Use (item) with (item)\"\n"
          "Players may use items they currently hold by inputting use and "
          "the desired item. A correct command would be \"Use Radio\".\n"
          "\nRarely, some items can be used together by inputting “Use "
          "(item) with (item)\". A correct command would be \"Use USB with "
          "Laptop\".\n"
          "\nFinally, if the use command does not result in an outcome the " 
          "player will receive a hint.\n"
          "\n\"Inventory\"\n"
          "Inputting \"Inventory\" will display the items currently held by the "
          "player.\n"
          "\n\"Wallet\"\n"
          "Inputting the \"Wallet\" command will provide the player with the "
          "amount of cash in their wallet.\n")
    print(" OTHER INPUTS ".center(40,"*"))
    print("\n\"Tutorial\"\n"
          "The player can enter the input \"Tutorial\" at any time to view all "
          "this information again.\n"
          "\n\"Quit\"\n"
          "If \"Quit\" is inputted by the player, the game will end, and the "
          "player will return to the main menu.\n")

def user_stats():
    """Displays player profiles sorted by lowest scores (best scores)"""
    print("Player Stats".center(40, "*"))
    profiles = []
    with open("player_profiles.txt", "r") as file:
        for line in file:
            profile_data = line.strip().split("|")
            profile_dict = {"username": profile_data[0],
                            "wallet total": int(profile_data[1]),
                            "best score": int(profile_data[2])}
            profiles.append(profile_dict)
    sorted_profiles = sorted(profiles, key=lambda x: (x["best score"]
                                                      if x["best score"] != 0
                                                      else float('inf')))
    count = 0
    for profile in sorted_profiles:
        count += 1
        print(f"{count}: {profile['username']} - Wallet Total: ${profile['wallet total']}, "
            f"Best Score: {profile['best score']}")
        print("")

def yes_or_no():
    """Gets the user to return y or n for yes/no"""
    user_input = ""
    while user_input not in ["y", "n"]:
        try:
            user_input = input("\"y\" for yes, \"n\"for no\n").lower()
        except:
            print("invalid input detected")
    return user_input

def description(current_room):
    """Describes the current room and it's contents to the player"""
    print("You find yourself in "+current_room["description"])
    print("From your best guess it's a " +current_room["room"])
    if current_room["north"] == "nothing":
        pass
    else:
        print("To the North you can see a "+current_room["north"])
    if current_room["south"] == "nothing":
        pass
    else:
        print("To the South you you can see a "+current_room["south"])
    if current_room["east"] == "nothing":
        pass
    else:
        print("To the East you can see a "+current_room["east"])      
    if current_room["west"] == "nothing":
        pass
    else:
        print("To the West you can see a "+current_room["west"])
    if len(current_room["items"]) != 0:
        print("\nThe following items stand out to you:\n")
        for items in current_room["items"]:
            print(items["item"]+" (it looks like " \
                    + items["description"]+")\n")
    else:
        print("There doesn't seem to be any interesting items\n")
                        
def move(cmd, current_room, rooms):
    """Trys to move in the given direction"""
    if cmd in current_room:
        if current_room[cmd] != "nothing":
            for room in rooms:
                if room["room"] == current_room[cmd]:
                    return room
    else: print("You can't move in that direction.")
    return current_room

def take(cmd, current_inventory, current_room, rooms, chosen_profile):
    """Attempts to take an item from a room's inventory and place it in the
      character's inventory"""
    if chosen_profile["wallet total"] >= 10:
        if len(current_inventory) == 3:
            print("\nYou can't pick anything else up.\n")
        elif cmd not in [item["item"] for item in current_room["items"]]:
            print("\nThere is nothing to take.\n")
        else:
            for item in current_room["items"]:
                if item["item"] == cmd:
                    current_inventory.append(item)
                    chosen_profile["wallet total"] -= 10
                    current_room["items"].remove(item)
                    item["use count"] = 0 
                    print("\nYou paid $10 and picked up " + cmd + ".\n")
                    break
        for room in rooms:
            if room["room"] == current_room["room"]:
                room.update(current_room)
                break
    else:
        print("You don't have enough in your wallet to pay for that.")
    return current_inventory, current_room, rooms, chosen_profile

def drop(cmd, current_inventory, current_room, rooms, chosen_profile):
    """Attempts to drop an item from the character's inventory and place it 
    in the current room"""
    for item in current_inventory:
        if item["item"] == cmd:
            if item["use count"] == 0:
                chosen_profile["wallet total"] += 5
                print("\nyou recived a $5 refund for not using the item\n")
            current_inventory.remove(item)
            dropped_item = item.copy()
            dropped_item.pop("use count")
            current_room["items"].append(dropped_item)
            print("\nYou drop " + cmd + ".\n")
            break
    else:
        print("\nYou don't have that item.\n")
    for room in rooms:
        if room["room"] == current_room["room"]:
            room.update(current_room)
            break
    return current_inventory, current_room, rooms, chosen_profile

def use(item1, current_inventory, current_room, item2=None):
    """Attempts to use a single item by  to get a hint or win the 
    game. Also attempts to use two items together"""
    if item2 is None:
        if item1 not in [item["item"] for item in current_inventory]:
            print("You do not have a " +item1+ ".\n")
            return current_inventory, current_room
        for item in current_inventory:
            if item["item"] == item1:
                item1 = item
                item["use count"] = 1
                break
        if item1["escape item"] == "yes" and current_room["escape room"] == \
            "yes":
            print("Congratulations! You WIN!")
            current_room = "outside"
            return current_inventory, current_room
        print("\nHint unlocked: "+item1["hint"]+"\n")
        return current_inventory, current_room
    if item1 not in [item["item"] for item in current_inventory]:
        print("You do not have a " +item1+ ".\n") 
        return current_inventory, current_room 
    if item2 not in [item["item"] for item in current_inventory]:
        print("You do not have a " +item2+ ".\n")
        return current_inventory, current_room
    if item1 or item2 == "rusty can opener" and item1 or item2 == \
        "can of baked beans":
        print("You use the the the rusty can opener to open the can of baked "
                "beans and a ornate key drops to the floor!")
        current_room["items"].append({
            "item": "ornate key",
            "description": "This sure is a fancy looking key",
            "hint": "Perhaps the lock style would match the key's style",
            "escape item": "yes"})  
        for item in current_inventory:
            if item["item"] == item1:
                current_inventory.remove(item)
                if item1 == "rusty can opener":
                    print("The rusty can opener breaks.")
                elif item1 == "can of baked beans":
                    print("You throw away the can of baked beans.")
                break
        for item in current_inventory:
            if item["item"] == item2:
                current_inventory.remove(item)
                if item2 == "rusty can opener":
                    print("The rusty can opener breaks.")
                elif item2 == "can of baked beans":
                    print("You throw away the can of baked beans.")
                break
        return current_inventory, current_room
    print("Nothing happens.")
    return current_inventory, current_room

def update_player_profile(username, wallet_total, best_score):
    """Updates a specific player profile in the palyer profile file"""
    with open("player_profiles.txt", "r") as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        profile_data = line.strip().split("|")
        if profile_data[0] == username:
            lines[i] = f"{username}|{wallet_total}|{best_score}|\n"
            break
    with open("player_profiles.txt", "w") as file:
        file.writelines(lines)

def main_game(chosen_profile):
    """Main gaim logic, plays the game and calls other functions as needed"""
    old_best_score = chosen_profile["best score"]
    rooms = read_setup_files()
    current_room = rooms[0]
    current_inventory = []
    if chosen_profile["wallet total"] < 30:
        chosen_profile["wallet total"] = 30
    score = 0
    if chosen_profile["best score"] == 0:
        print("Would you like to view the tutorial before starting?")
        y_or_n = yes_or_no()
        if y_or_n == "y":
            tutorial()
    print(" MULTI MADDNESS TEXT GAME ".center(40,"*"))
    print("You awake dazed and confused")
    while current_room != "outside":
        if score != 0:
            print(f" {score} ".center(40,"*"))
        description(current_room)
        cmd = input("Enter a command:\n").lower().split()
        cmd = " ".join(cmd)
        if cmd == "tutorial":
            tutorial()
        elif cmd == "quit":
            print("Are you sure you want to quit?")
            y_or_n = yes_or_no()
            if y_or_n == "y":
                return 0
        elif cmd.startswith("move"):
            print("")
            current_room = move(cmd[5:], current_room, rooms)
            score += 1
        elif cmd.startswith("take"):
            current_inventory, current_room, rooms, chosen_profile = \
                take(cmd[5:], current_inventory, current_room, rooms, \
                     chosen_profile)
            score +=1
        elif cmd.startswith("drop"):
            current_inventory, current_room, rooms, chosen_profile = \
                drop(cmd[5:], current_inventory, current_room, rooms, \
                     chosen_profile)
            score +=1      
        elif cmd.startswith("use"):
            items = cmd[4:].split(" with ")
            if len(items) == 1:
                current_inventory, current_room = \
                    use(items[0], current_inventory, current_room)
                score += 1
            if len(items) == 2:
                current_inventory, current_room = \
                    use(items[0], current_inventory, current_room, items[1])
                score += 1
        elif cmd == "wallet":
            print("\nYou have $" +str(chosen_profile["wallet total"])+ \
                  " in your wallet.\n")
            score +=1
        elif cmd == "inventory":
            if len(current_inventory) >=1:
                print("You look in your inventory and see the following:")
                for item in current_inventory:
                    print(item["item"])
                print("")
            else:
                print("You don't appear to have anything in your "
                      "inventory.\n")
            score +=1
        else:
            print("Unknown command, please try again.")
    chosen_profile["wallet total"] += 40
    print("Your score was "+str(score))
    chosen_profile["best score"] = score
    if old_best_score != 0:
        if chosen_profile["best score"] < old_best_score:
            update_player_profile(chosen_profile["username"], \
                                  chosen_profile["wallet total"],\
                                  chosen_profile["best score"])
            print("You beat your old best score of " + str(old_best_score)\
                   + "!")
        else:
            update_player_profile(chosen_profile["username"], \
                                  chosen_profile["wallet total"], \
                                  old_best_score)
    else:
        update_player_profile(chosen_profile["username"], \
                              chosen_profile["wallet total"],\
                              chosen_profile["best score"])
        print("Added new best score.")
    return 0


        
# Main loop of the file, calls other fucntions which perform game functions
if not os.path.isfile("room_setup.txt") or not os.path.isfile("item_setup.txt"):
    file_setup()
menu_input = 0
while menu_input not in range(1,6):
    print(" MAIN MENU ".center(40,"*"))
    try:
        menu_input = int(input(
            "Welcome to my amazing multi madness text game!\n"
            "\nPlease enter the number from the following options:\n"
            "1: New game\n"
            "2: Tutorial\n"
            "3: View user stats\n"
            "4: Restore default room and item setups\n"
            "5: Quit program\n"))
    except:
        print("invalid user input\n")
    if menu_input == 1:
        menu_input = main_game(player_profile())
    if menu_input == 2:
        tutorial()
        menu_input = 0
    if menu_input == 3:
        user_stats()
        menu_input = 0
    if menu_input == 4:
        print("Are you sure you want restore setup files?")
        setup_yes_no = yes_or_no()
        if setup_yes_no == "y":
            file_setup()
            print("Setup files restored.\n")
            menu_input = 0                               
        else:
            menu_input = 0
    if menu_input == 5:
        print("Are you sure you want to exit the game?")
        yes_no = yes_or_no()
        if yes_no == "y":
            exit()
        else:
            menu_input = 0
