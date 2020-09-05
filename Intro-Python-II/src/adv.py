import sys
import time
import textwrap
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


def steady_print(text):
    for character in text:
        sys.stdout.write(character)
        time.sleep(.05)
    return ""


def display_location(loc):
    print(steady_print(f"Current location: {room[loc].name}"))
    print(steady_print(room[loc].description))


def outside_choice():
    options = ["y", "n"]
    choice = ""
    while choice not in options:
        choice = input("Do you dare enter the cave? [y, n]:")
        if choice == "y":
            global loc
            loc = room["foyer"].name
            return steady_print("You take a deep breath and enter...")
        elif choice == "n":
            print(steady_print("Game Over."))
            quit()
        else:
            print(steady_print("I didn't understand that."))


def in_cave_choice(location):
    while True:
        choice = input("Which way do you go? [n, s, e, w]:")
        attrib = f"{choice}_to"
        next_room = room[location].attrib
        if next_room:
            global loc
            loc = next_room.name
            return ""
        else:
            print(steady_print(
                f"You run in to solid wall. Confused, you return to the {room[loc].name}..."))


#
# Main
#

print(steady_print("Welcome treasure hunter..."))

# Start
loc = room["outside"].name

while True:
    if loc == room["outside"].name:
        display_location(loc)
        outside_choice()
    else:
        display_location(loc)
        in_cave_choice(loc)


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
