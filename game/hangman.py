# ------------------------------------------------------------------------------
# Import Packages
# ------------------------------------------------------------------------------
import random

# List of words
word_list = ["Python", "Hangman", "Entwickler", "Tastatur", "Test", "Spieleabend", "Liebe"]

# function to choose random word
def choose_word(word_list):
    return random.choice(word_list).lower()

# testing function
print("Das ausgewählte Word ist:", choose_word(word_list))