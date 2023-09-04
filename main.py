import random

# This function generates a random number between 1 and 6


def roll():
    min_value = 1
    max_value = 6

    # Generate a random number between the minimum and maximum values
    roll = random.randint(min_value, max_value)

    return roll


# This code gets the number of players from the user
while True:
    # Get the number of players from the user
    players = input("Enter the number of players (2 - 4): ")

    # Check if the input is a digit
    if not players.isdigit():
        print("Invalid, try again.")
        continue

    # Convert the input to an integer
    players = int(players)

    # Check if the number of players is between 2 and 4
    if not (2 <= players <= 4):
        print("Must be between 2 - 4 players.")
        continue

    # Break out of the loop
    break

# Create a list to store the scores of each player
player_scores = [0 for _ in range(players)]

while True:
    # This loop iterates over the players
    for player_idx in range(len(player_scores)):
        # Print the player's number and total score
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")

        # Initialize the current score for the player
        current_score = 0

        # This loop continues until the player decides to stop rolling or rolls a 1
        while True:
            # Ask the player if they want to roll the dice
            should_roll = input("Would you like to roll (y)? ")

            # If the player does not want to roll the dice, break out of the loop
            if should_roll.lower() != "y":
                break

            # Roll the dice and get the value
            value = roll()

            # If the value is 1, the player's turn is over
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break

            # Otherwise, add the value to the player's current score
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your current score is", current_score)

        # Add the current score to the player's total score
        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

        # Find the index of the player with the maximum score
        winning_idx = player_scores.index(max(player_scores))

    # Print the winner
    print("Player number", winning_idx + 1,
          "is the winner!")

    while True:
        play_again = input("Would you like to play again? (y/n) ")

        # If the user does not want to play again, break out of the loop
        if play_again.lower() == "y":
            # Reset the scores
            player_scores = [0 for _ in range(players)]
            players = int(input("Enter the number of players (2 - 4): "))
        break
