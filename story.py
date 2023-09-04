# This line of code opens the file `story.txt` and reads its contents into the variable `story`.
# ...the `with` statement ensures that the file is closed properly after it is read.
# The " as f " clause assigns the file object to the variable f.
with open("story.txt", "r") as f:
    # The read() method reads the contents of a file and returns it as a string.
    story = f.read()
    words = []  # This list will store the words in the story.
    start_word = -1  # Keeps track of the start index of the current word.
    start_target = "<"  # This is the character that marks the start of a word.
    end_target = ">"  # This is the character that marks the end of a word.

    for i, character in enumerate(story):
        if character == start_target:
            # If the current character is the start target, set `start_word` to the current index.
            start_word = i
        if character == end_target and start_word != -1:
            # Create a new word from the characters between the start and end targets.
            word = story[start_word: i + 1]
            words.append(word)  # Add the word to the list `words`.
            # Set `start_word` to -1 to indicate that we are no longer at the start of a word.
            start_word = -1
