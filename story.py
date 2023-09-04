# This line of code opens the file `story.txt` and reads its contents into the variable `story`.
# ...the `with` statement ensures that the file is closed properly after it is read.
# The " as f " clause assigns the file object to the variable f.
with open("story.txt", "r") as f:
    # The read() method reads the contents of a file and returns it as a string.
    story = f.read()
    words = set()  # This list will store the words in the story.
    start_word = -1  # Keeps track of the start index of the current word.
    start_target = "<"  # This is the character that marks the start of a word.
    end_target = ">"  # This is the character that marks the end of a word.

    # This loop iterates over the characters in the string `story`.
    # If the current character is the start target, `<`, set the variable `start_word` to the current index.
    # If the current character is the end target, `>`, and the variable `start_word` is not -1,
    # then create a new word from the characters between the start and end targets, and add it to the list `words`.
    # Then, set the variable `start_word` to -1.
    # enumerate() method returns an iterator that enumerates the elements of a sequence.
    for i, character in enumerate(story):
        if character == start_target:
            # If the current character is the start target, set `start_word` to the current index.
            start_word = i
        if character == end_target and start_word != -1:
            # Create a new word from the characters between the start and end targets.
            word = story[start_word: i + 1]
            words.add(word)  # Add the word to the list `words`.
            # Set `start_word` to -1 to indicate that we are no longer at the start of a word.
            start_word = -1

# This dictionary will store the words in the story and their corresponding answers.
answers = {}
for word in words:
    # This loop iterates over the words in the `words` set.
    answer = input("Enter a word for " + word + ": ")
    # This line of code prompts the user to enter a word for the current word in the `words` set.
    answers[word] = answer
    # This line of code adds the word and its corresponding answer to the `answers` dictionary.

for word in words:
    # This loop iterates over the words in the `words` set.
    story = story.replace(word, answers[word])
    # This line of code replaces the current word in the `story` string with its corresponding answer from the `answers` dictionary.

print(story)
# This line of code prints the `story` string.
