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

# function to check the letter
def check_guess(word, guessed_letters, guess):
    if guess in word: 
        print(f"Gut gemacht! '{guess}' ist im Word enthalten.")
        guessed_letters.append(guess)
        return True
    else: 
        print(f"Leider ist '{guess}' nicht im Wort :(")
        return False
    
# testing the check
choose_word = choose_word(word_list)
guessed_letters = []
print(f"Das geheime Wort ist: {choose_word}")

spieler_buchstabe = get_player_guess()
check_guess(choose_word, guessed_letters, spieler_buchstabe)

# showing the word with guesses letters
print("Aktuelles Wort:", display_word(choose_word, guessed_letters))
