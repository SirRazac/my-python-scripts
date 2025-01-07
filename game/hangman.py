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

# function to display word with _ _ _
def display_word(word, guessed_letters):
    # if letter is guessed show it. Otherwise show "_"
    return" ".join([letter if letter in guessed_letters else "_" for letter in word])

# testing function
chosen_word = "python"
guessed_letters = []
print("Aktuelles Wort:", display_word(chosen_word, guessed_letters))

# example
guessed_letters = ['p', 'o']
print("Nach dem Raten:", display_word(chosen_word, guessed_letters))

# function for asking a letter 
def get_player_guess():
    while True:
        guess = input("Rate einen Buchstaben: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else: 
            print("Ungültige Eingabe. Bitte einen einzelnen Buchstaben eingeben.")

# testing function
spieler_buchstabe = get_player_guess()
print(f"Du hast den Buchstaben '{spieler_buchstabe}' gewählt.")
