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

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) <= max_score:

    for players_inx in range(players):
        current_score = 0

        while True:
            should_roll = input("Would you roll the dice? (y)")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You've done 1, pass your turn")
                current_score == 0
                break
            else:
                current_score += value
                print("You've scored", value)

            print("Your score is:", current_score)

        player_score[players_inx] += current_score
        print("Your total score is:", player_score[players_inx])
