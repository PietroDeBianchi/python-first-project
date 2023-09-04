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


# Define a variable called `value` and store the output of the `roll()` function
value = roll()

# Print the value of the `value` variable
print(value)
