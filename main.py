# Create a Hangman Game
# Provide the user with 10 lives.

# Imports
from random import randint
from art import stages
from words import word_list
# Print hangman icon to and introduce game:
print(stages[0])
print("Welcome to HANGMAN.")
print("The aim of the game is to guess the word I am thinking, before the noose tightens around your neck.\n")
print("Let's play.\n")
# Pick a random word from 'word_list' and make .lower():
chosen_word = (word_list[randint(0, len(word_list) - 1)]).lower()
# Cast 'chosen_word' to list and save as 'chosen_word_list':
chosen_word_list = list(chosen_word)
# For testing print 'chosen_word':
print(f"The chosen word is: {chosen_word}\n")
# Create an empty list showing dashes to indicate word length and name 'spaces_list':
spaces_list = []
for i in chosen_word:
    spaces_list.append("-")
# Print 'spaces_list':
print(f"I'm thinking of a word that looks like this:\n\n{spaces_list}\n")
print("Try and guess what it is.\n")
# Give the player 6 lives:
lives = 10
# Create empty list to keep track of player guesses:
guesses = []
# Create boolean for playing:
playing = True
# While player still has lives:
while playing:
    # Check if lives are greater than 0:
    if lives > 0:
        # Ask user for a letter and save as 'guess':
        guess = input("Pick a letter: ")
        # If player 'guess' in 'chosen_word' and not previously 'guessed':
        if guess in chosen_word and guess not in guesses:
            guesses.append(guess)
            for i in range(len(chosen_word)):
                if guess == chosen_word[i]:
                    spaces_list[i] = guess
            # If 'spaces_list' is equal to 'chosen_word_list' player wins:
            if spaces_list == chosen_word_list:
                print(f"\n{spaces_list}")
                print("\nCongratulations. You WIN!")
                print(f"The word I was thinking of was: {chosen_word}")
                playing = False
            # Else 'spaces_list' not equal to 'chosen_word_list' player tries again:
            else:
                print(f"\n{spaces_list}")
                print("\nYour guess is in the word. Try another.\n")
                continue
        # Else if guess in 'chosen_word' and already in 'guesses:'
        elif guess in chosen_word and guess in guesses:
            print(f"\n{spaces_list}")
            print("\nYou have already correctly guessed that letter.")
            print("You have not lost a life, but be more careful next time.")
            print("Try again.\n")
            continue
        # Else if guess not in 'chosen_word' and already in 'guesses:'
        elif guess not in chosen_word and guess in guesses:
            print(f"\n{spaces_list}")
            print("\nYou have already incorrectly guessed that letter.")
            print("The noose is getting tighter.")
            print(f"\n{stages[lives]}")
            print("Try again.\n")
            lives -= 1
            continue
        # Else if player 'guess' not in 'chosen_word':
        elif guess not in chosen_word:
            guesses.append(guess)
            print(f"\n{spaces_list}")
            print("\nThat letter is not in the word.")
            print("You are one step closer to the end.")
            print(f"\n{stages[lives]}")
            print("Try again.\n")
            lives -= 1
            continue
    # Else player has no more lives left.
    else:
        print(f"\n{spaces_list}")
        print("\nWrong again.")
        print("You are out of chances.")
        print(f"The word I was thinking of was: {chosen_word}")
        print("It's the long drop for you...")
        print(f"\n{stages[lives]}\n")
        playing = False
# Player not playing
print("\nGAME OVER.")
