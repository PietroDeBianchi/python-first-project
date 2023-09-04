# Import the random module from PiP
import random

# Define a function called `roll()`


def roll():
    # Define the minimum and maximum values for the dice roll
    min_value = 1
    max_value = 6

    # Generate a random number between the minimum and maximum values
    roll = random.randint(min_value, max_value)

    # Return the random number
    return roll


while True:
    players = input("enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 1 < players <= 4:
            print("players choosen correctly")
            break
        else:
            print("invalid players number must be between 2 - 4")
print(players)
