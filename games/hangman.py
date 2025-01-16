# ------------------------------------------------------------------------------
# Import Packages
# ------------------------------------------------------------------------------
import random

# ------------------------------------------------------------------------------ 
# Game
# ------------------------------------------------------------------------------
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
        guess = input("Rate einen Buchstaben oder das gesamte Wort: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess, "letter"
        elif len(guess) > 1 and guess.isalpha():
            return guess, "word"
        else: 
            print("Ungültige Eingabe. Bitte einen einzelnen Buchstaben oder ein gültiges Wort eingeben.")

# function to check the letter
def check_guess(word, guessed_letters, guess, guess_type):
    if guess_type == "letter":
        if guess in word:
            print(f"Gut gemacht! '{guess}' ist im Wort enthalten.")
            guessed_letters.append(guess)
            return True
        else:
            print(f"Leider ist '{guess}' nicht im Wort :(")
            return False
    elif guess_type == "word":
        if guess == word:
            print(f"Super! Du hast das gesamte Wort richtig erraten: {guess}")
            return True
        else:
            print(f"Leider war das nicht das richtige Wort :( Versuche es weiter!")
            return False

# game function
def play_game():
    word = choose_word(word_list)
    guessed_letters = []
    attempts = 6
    
    print("Willkommen zu Hangman!")
    
    while attempts > 0:
        print("\nAktuelles Wort: ", display_word(word, guessed_letters))
        guess, guess_type = get_player_guess() 
        
        if guess_type == "word":
            if guess == word:
                print(f"Herzlichen Glückwunsch! Du hast das gesamte Wort '{word}' richtig erraten!")
                break
            else:
                print(f"Leider war das nicht das richtige Wort. Versuche es weiter!")
                attempts -= 1
        else:
            if check_guess(word, guessed_letters, guess, guess_type):
                if all(letter in guessed_letters for letter in word):
                    print(f"Herzlichen Glückwunsch! Du hast das Wort '{word}' erraten!")
                    break
            else:
                attempts -= 1
                print(f"Du hast noch {attempts} Versuche übrig.")
            
        if attempts == 0:
            print(f"Leider hast du verloren! Das Wort war: {word}")


play_game()    
