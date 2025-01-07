# ------------------------------------------------------------------------------
# Import Packages
# ------------------------------------------------------------------------------
import random

# List of words
word_list = ["Python", "Hangman", "Entwickler", "Tastatur", "Test", "Spieleabend", "Liebe"]

# function to choose random word
def choose_word(word_list):
    return random.choice(word_list).lower()


# function to display word with _ _ _
def display_word(word, guessed_letters):
    # if letter is guessed show it. Otherwise show "_"
    return" ".join([letter if letter in guessed_letters else "_" for letter in word])

# function for asking a letter 
def get_player_guess():
    while True:
        guess = input("Rate einen Buchstaben: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else: 
            print("Ungültige Eingabe. Bitte einen einzelnen Buchstaben eingeben.")

# function to check the letter
def check_guess(word, guessed_letters, guess):
    if guess in word: 
        print(f"Gut gemacht! '{guess}' ist im Word enthalten.")
        guessed_letters.append(guess)
        return True
    else: 
        print(f"Leider ist '{guess}' nicht im Wort :(")
        return False

# game function
def play_game():
    word = choose_word(word_list)
    guessed_letters = []

    while True:
        print("Aktuelles Wort:", display_word(word, guessed_letters))
        guess = get_player_guess()
        if check_guess(word, guessed_letters, guess):
            print("Aktuelles Wort:", display_word(word, guessed_letters))

        # check if play has guessed the hole word
        if all(letter in guessed_letters for letter in word):
            print(f"Super, du hast das Wort '{word}' erraten! :)")
            break

play_game()    
