"""
Matthew Garchik
Hangman
February 2020
"""

import random
# Hangman game

# PSEUDOCODE
# setup your game by doing the following
# make a word list for your game
# grab a random word from your list and store it as a variable


# in a loop, do the following
# display the hangman using the gallows
# display the used letters so the user knows what has been selected
# display the length of the word to the user using blank spaces and used letters
# prompt the user to guess a letter
# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect_guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all the correct letters, tell the user they won

# ask if they want to play again

gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]

my_word_list = ["delta", "earnings", "beta", "investment", "loss",
                "interest", "bonds", "yield", "dividend", "option"
                , "money", "funds", "savings", "retirement", "tax"]


def play():
    lives_lost = 0
    my_word = my_word_list.pop(random.randrange(len(my_word_list)))
    print(my_word)
    my_list = []
    for i in range(len(my_word)):
        my_list.append("_")
    abcs = [chr(x) for x in range(65, 65 + 26)]
    used_abcs = []
    while lives_lost < 6:
        for i in my_list:
            print(i, end=" ")
        print()
        guess = input("Guess Letter")
        while guess.upper() in used_abcs:
            guess = input("You have used that letter, guess again")
        while guess.upper() not in abcs:
            guess = input("That is not a letter, guess again")
        used_abcs.append(guess.upper())

        print("Guessed Letters:")
        for letter in used_abcs:
            print(letter, end=" ")

        guess = guess.lower()

        if str(guess) in my_word:
            for i in range(len(my_word)):
                if my_word[i] == guess:
                    my_list[i] = guess.lower()

        else:
            lives_lost += 1

        print("")

        for i in my_list:
            print(i, end=" ")

        print(gallows[-(lives_lost + 1)])

        if "_" not in my_list:
            print("You Win!")
            new_input = input("Press any letter to restart, or hit space to exit")
            if new_input.upper() in abcs:
                play()
                print(my_word)
            elif new_input == " ":
                quit()
        if lives_lost >= 6:
            print("You Lose!")
            new_input = input("Press any letter to restart, or hit space to exit")
            if new_input.upper() in abcs:
                play()
                print(my_word)
            elif new_input == " ":
                quit()


print("Welcome to Matthew Garchik's finance hangman!")
play()