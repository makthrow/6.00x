from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """

    # Create a new variable to store the maximum score seen so far (initially 0)
    maxscore = 0
    # Create a new variable to store the best word seen so far (initially None)
    bestword = None
    # For each word in the wordList
    for w in wordList:
        # If you can construct the word from your hand
        if isValidWord(w, hand, wordList):

        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
            # Find out how much making that word is worth
            score = getWordScore(w, HAND_SIZE)
            # If the score for that word is higher than your best score
            if score > maxscore:
                # Update your best score, and best word accordingly
                maxscore = score
                bestword = w
    # return the best word you found.
    return bestword

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    """
    # TO DO ... <-- Remove this comment when you code this function

#
# Problem #8: Playing a game
#
#

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1

    use the HAND_SIZE constant to determine the number of cards in a hand.
    """
    handPlayed = False

    while True:
        userInput = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if userInput is not "e" and userInput is not 'r' and userInput is not 'n':
            #print userInput
            print "Invalid command."
            continue
        elif userInput == 'e':
            break
        elif userInput == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand.copy(), wordList, HAND_SIZE)

            handPlayed = True
        elif userInput == 'r':
            if not handPlayed:
                print "You have not played a hand yet. Please play a new hand first!"
                continue
            else:
                playHand(hand.copy(), wordList, HAND_SIZE)




#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


print compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList)
print compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList)
print compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList)
print compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList)

