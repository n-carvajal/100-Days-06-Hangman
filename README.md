# 100 Days of Python Code

## Project 6: Hangman

Create a hangman game to be played between one player and the CPU.

### Gameplay

The CPU chooses a word, and draws a number of dashes equivalent to the number of letters in the chosen word.
The player tries to guess what it is one letter at a time.
If the player guesses a letter than occurs in the word.
The CPU replaces the corresponding dash with the letter guessed.
If the word does not contain the guessed letter, the CPU draws one element of a hangman’s gallows.
As the game progresses, a segment of the gallows and of a victim is added for every letter guessed incorrectly.
The player can make 6 incorrect guesses before the gallows and the hangman are completed.

The game ends when either the player guesses the word or the hangman drawing is completed.