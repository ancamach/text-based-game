def move_player(direction, current_loc, exits):
    if direction in exits[current_loc]:
        return exits[current_loc][direction]
    else:
        print("You can't go that way.")
        return current_loc
    

def main():
    locations = {
        "dark room": {
            "description": "You are in a dark room. There is a door to the north.",
            "items": ["key"]
        },
        "hallway": {
            "description": "You are in a long hallway. There is a door to the south and to the east.",
            "items": []
        },
        "mystery room": {
            "description": "You are in a mysterious room, full of what appears to be magical equipment and weird elixirs. There are doors to the east and the north.",
            "items": ["staff", "weird elixir", "ominous grimoire"]
        },
        "balcony": {
            "description": "The door leads you to a balcony overlooking a massive cliff. There is a door to the south.",
            "items": []
        },
        "laboratory": {
            "description": "You are in a laboratory, surrounded by alchemy equipment and spell ingredients. There is a summoning circle in the middle of the room and a door to the west.",
            "items": ["magic broom"]
        }
    }
    exits = {
        "dark room": {"north": "hallway"},
        "hallway": {"south": "dark room", "east": "mystery room"},
        "mystery room": {"west": "hallway", "north": "balcony", "east": "laboratory"},
        "laboratory": {"west": "mystery room"},
        "balcony": {"south": "mystery room"}
    }
    inventory = []
    current_location = "dark room"
    gameover = False
    door_locked = True

    print("Welcome to the Text Adventure Game!")
    input("Press enter to start...")

    while not gameover:
        command = input("> ").lower()
        if command == "exit":
            break
        elif command == "look":
            print(locations[current_location]["description"])
            if locations[current_location]["items"]:
                print("You see: " + ", ".join(locations[current_location]["items"]))
        elif command == "help":
            print("Commands you can use: look, take [item], use [item], inventory, exit, use cardinal points to move")
        elif command.startswith("take"):
            item_name = command.split(" ", 1)[1]
            if item_name in locations[current_location]["items"]:
                locations[current_location]["items"].remove(item_name)
                inventory.append(item_name)
                print("You take the " + item_name)
            else:
                print("There is no " + item_name + " here.")
        elif command.startswith("use"):
            item_to_use = command.split(" ", 1)[1]
            if item_to_use in inventory:
                if current_location == "mystery room" and item_to_use == "key":
                    print("You use the key to unlock the east door!")
                    exits["mystery room"]["east"] = "laboratory"
                    print("The east door is now unlocked!")
                    door_locked = False
                elif item_to_use == "weird elixir":
                    print("You drink the weird elixir. It tastes strange...")
                    print("Maybe drinking random liquids is not the best idea. Game over!")
                    gameover = True
                elif item_to_use == "ominous grimoire":
                    print("Using the grimoire causes wings to sprout from your back!")
                else:
                    print("You can't use that here.")
        elif command == "inventory":
            if inventory:
                print("Inventory: " + ", ".join(inventory))
            else:
                print("Your inventory is empty.")
        elif command in exits[current_location]:
            new_location = move_player(command, current_location, exits)
            if new_location != current_location:
                if door_locked and new_location == "laboratory":
                    print("This door is locked. You need a key.")
                else:
                    print("You move to the " + command)
                    current_location = new_location
                    print(locations[current_location]["description"])
                    if current_location == "balcony":
                        if "magic broom" in inventory:
                            print("You fly away using the magic broom. Congratulations! You've won the game!")
                            gameover = True
                        if "ominous grimoire" in inventory:
                            print("Thanks to your new wings you can fly away into the sunset. Congratulations! You've won the game!")
                            gameover = True
        else:
            print("I don't understand that command.")

if __name__ == "__main__":
    main()