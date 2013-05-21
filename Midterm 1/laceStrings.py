def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """

    newStr = ''
    s1List = list(s1)
    s2List = list(s2)

    while s1List or s2List:
        if s1List:
            newStr += s1List.pop(0)
        if s2List:
            newStr += s2List.pop(0)


    return newStr

