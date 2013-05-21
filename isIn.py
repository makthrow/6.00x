def lenRecur(aStr):
    # base case = str is empty
    if aStr == '':
        return 0
    return 1 + lenRecur(aStr[0:-1])

def isIn(char, aStr, ''):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # cut string in half.
    # compare to middle character
    """
    note, in cases of even number length string
    where there are two middle characters,
    this takes the higher middle character
    """
    # base case:
    if aStr == '':
        print "char %r is not in string: %r" % (char, aStr)
        return False
    middlechar = ''
    middlecharIndex = lenRecur(aStr) / 2
    middlechar = aStr[middlecharIndex]

    if middlechar == char:
        print "char %r is in string: %r" % (char, aStr)
        return True
    # use smaller half, not including middlechar
    elif char < middlechar:
        aStr = aStr[:middlecharIndex]
    # use larger half, not including middlechar
    elif char > middlechar:
        aStr = aStr[middlecharIndex + 1:]
    return isIn(char, aStr, ogStr )


isIn('y', 'abcdefghijklnop')
