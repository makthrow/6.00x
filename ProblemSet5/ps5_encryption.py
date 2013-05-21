# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    returndict = {}
    #reference alphabet strings
    abcLo = string.ascii_lowercase * 2
    abcUp = string.ascii_uppercase * 2

    for l in abcLo:
        # find letter index in abcLo
        index = abcLo.find(l)
        returndict[l] = abcLo[index + shift]
    for l in abcUp:
        index = abcUp.find(l)
        returndict[l] = abcUp[index + shift]
    return returndict

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    encodedStr = ''
    for l in text:
        if l.isalpha():
            newletter = coder[l]
            encodedStr += newletter
        else:
            encodedStr += l
    return encodedStr

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """

    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
"""
pseudocode for decryption:

split text into words separated by whitespace, put in a list
-take the first word in the list, begin applying shifts from 1-25


  if a valid shifted word is found,
    note the shift
    move on to the second word
    test second word with that shift
    if it is valid:
      test the third word with that shift
        if it is valid, test fourth, and so on
    if a tested word is not valid with a shift, then go back to the first word and keep testing shifts again

"""
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    shiftRecords = {}
    for n in range(1,26):
        shiftRecords[n] = 0
   # print shiftRecords
    bestShift = 0
    mostWords = 0
    text = text.split()
    for shift in range(1,26):
      #  print "shift: %d" % shift
        for word in text:
            if isWord(wordList, applyShift(word, shift)):
         #       print "word: %s" % applyShift(word, shift)
                shiftRecords[shift] += 1
    # find which shift is the best
    for shift in shiftRecords:
       if mostWords < shiftRecords[shift]:
            bestShift = shift
            mostWords = shiftRecords[shift]
    return bestShift









def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    wordList = loadWords()
    text = getStoryString()
    shift = findBestShift(wordList, text)

    return applyShift(text, shift)




    return "Not yet implemented." # Remove this comment when you code the function

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()
    decryptStory()
