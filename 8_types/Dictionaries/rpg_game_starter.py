#*********** Global Variables **********
inventory = []  #an inventory, which is initially empty
current_room = 1  #start the player in room 1
#a dictionary linking a room to other room positions
rooms = {

    1: {"name": "Hall",
        "east": 2,
        "south": 3},

    2: {"name": "Bedroom",
        "west": 1,
        "south": 4,
        "item": "sword"},

    3: {"name": "Kitchen",
        "north": 1},

    4: {"name": "Bathroom",
        "north": 2}

}


def main() -> None:
    show_instructions()

    global current_room
    global inventory

    # Game loop - loop infinitely 
    while True:

        show_status()

        '''
        Get the player's next 'move'. 
        .split() breaks it up into an list array.
        Typing 'go east' would give the list:
        ['go','east'] '''

        move = []
        while len(move) == 0:
            move = input(">").lower().split()

        #if they type 'go' first
        if move[0] == "go":
            go_to_room(move)

        #if they type 'get' first
        if move[0] == "get":
            process_inventory(move)

        #if they type 'menu' first
        if move[0] == "menu":
            show_instructions()


def show_instructions() -> None:
    # comment
    print("RPG Game")
    print("========")
    print("Commands:")
    print("'go [direction]'")
    print("'get [item]'")
    print("'menu'")


def show_status() -> None:
    global current_room
    global inventory

    #print the player's current status
    print("---------------------------")

    print(f'You are in the "{rooms[current_room]["name"]}"')

    #print the current inventory
    print(f'Inventory : {str(inventory)}')
    #print an item if there is one
    if "item" in rooms[current_room]:
        print(f'You see a {rooms[current_room]["item"]}')

    print("---------------------------")


def go_to_room(move) -> None:
    global current_room

    # check that a direction is specified
    if len(move) == 1:
        print(f"Please indicate a direction")
    #check that they are allowed wherever they want to go
    elif move[1] in rooms[current_room]:
        #set the current room to the new room
        current_room = rooms[current_room][move[1]]
    #there is no door (link) to the new room
    else:
        print("You can't go that way!")


def process_inventory(move) -> None:
    global current_room
    global inventory

    # check that an item is specified
    if len(move) == 1:
        # noinspection SpellCheckingInspection
        print(f"Please indicate a item to get ")
    #if the room contains an item, and the item is the one they want to get
    elif "item" in rooms[current_room] and move[1] == rooms[current_room]["item"]:
        #add the item to their inventory
        inventory += [move[1]]
        #display a helpful message
        print(f"{move[1]} got!")
        #delete the item from the room
        del rooms[current_room]["item"]
    #otherwise, if the item isn't there to get
    else:
        #tell them they can't get it
        print(f"Can't get {move[1]}!")


if __name__ == "__main__":
    main()
