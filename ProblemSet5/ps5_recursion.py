# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.

    aStr: a string
    returns: a reversed string
    """
    # slice last letter off
    # return reverseString(str with last letter chopped)
    # base case: if aStr is empty, then stop
    if not aStr:
        return ''
    lastLetter = aStr[-1]
    text = aStr[:-1]
    return lastLetter + reverseString(text)

# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False

    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if not x:
        return True
    if not word:
        return False
    if x[0] == word[0]:
        word = word[1:]
        x = x[1:]
    elif x[0] != word[0]:
        word = word[1:]

    return x_ian(x, word)


#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately.
    """
    def gotoWordEnd(text, lineEnd):
        print "Text: %s, %r" % (text, lineEnd)
        if len(text) == lineEnd:
            return lineEnd
        if text[lineEnd] ==' ': # test if its a space
            return lineEnd
        lineEnd += 1

        return gotoWordEnd(text, lineEnd)

    # Base case: text is empty:
    if not text:
        return ''

    # check if we are on a current word.
    lineEnd = lineLength - 1
    print "lineEnd == %r" % lineEnd

    currentWord = ''
    if len(text) >= lineLength:
        currentWord = text[lineEnd]
        
       # current letter isn't empty. keep skipping forward
    # return lineLengthIndex of after the word ends
    print "current word == %s" % currentWord
    if currentWord:

        wordEnd = gotoWordEnd(text, lineEnd)
        print "wordEnd: %r" % wordEnd
        currentLine = text[:wordEnd] + "\n"
        print "currentLine: %s " % currentLine
        text = text[wordEnd + 1:]
    else:
        currentLine = text[:lineLength]
        text = text[lineLength:]
    return currentLine + insertNewlines(text, lineLength)

