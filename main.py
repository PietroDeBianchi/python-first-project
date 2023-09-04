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


# This code gets the number of players from the user
while True:
    # Get the number of players from the user
    players = input("enter the number of players (2-4): ")
    # Try to convert the number of players to an integer
    try:
        players = int(players)
        # If the number of players is between 2 and 4, break out of the loop
        if 1 < players <= 4:
            break
        # Otherwise, print an error message
        else:
            print("invalid players number must be between 2 - 4")
    # If the conversion to an integer fails, print an error message
    except ValueError:
        print("Invalid, must be a number")
# Print the number of players
print(players)
