#!/usr/bin/env python3
# exercises https://pythonbasics.org/exercises/

# define strings
firstname = "Bugs"
lastname = "Bunny"

# define our sequence
sequence = (firstname, lastname)

# join into new string
name = " ".join(sequence)
print(name)

words = ["How", "are", "you", "doing", "?"]
sentence = ' '.join(words)
print(sentence)


# Create a list of words and join them, like the example above.

# Try changing the seperator string from a space to an underscore.

sentence2 = '_'.join(words)
