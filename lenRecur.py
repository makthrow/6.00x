def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # base case = str is 0
    count = 1
    if aStr == '':
        return 0
    else:
        return count + lenRecur(aStr[0:-1])


print lenRecur('1234567890')

