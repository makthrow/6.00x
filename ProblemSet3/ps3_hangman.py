# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    # passed all conditions above. word is guessed
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter
        else:
            guessedWord += "_"
    return guessedWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    availableLetters = ''
    for letter in alphabet:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %r letters long" % len(secretWord)

    guessesLeft = 8
    lettersGuessed = []

    while isWordGuessed (secretWord, lettersGuessed) is not True and guessesLeft > 0:
        print "-----------"
        print "You have %r guesses left." % guessesLeft
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        guessLetter = raw_input("Please guess a letter: ").lower()


        # conditions
        # already guessed letter, keep guessesLeft same
        if guessLetter in lettersGuessed:

            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)


        # user guesses wrong, decrement guessesLeft
        elif guessLetter not in secretWord:
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            guessesLeft -= 1
            lettersGuessed.append(guessLetter)
        elif guessLetter in secretWord:
        # user guesses letter in word, keep guessesLeft same
            lettersGuessed.append(guessLetter)

            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
        else:
            print "Sorry, please try again."

    #end of game. either user guessed word or no guesses left
    print "-----------"
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was %s." % secretWord










# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)
