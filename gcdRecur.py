"""
AK's version
"def gcdRecur(a, b):

    larger = max(a, b)
    smaller = min(a, b)
   # print "larger: %r" % larger
   # print "smaller: %r" % smaller
    if smaller == 1 or larger == smaller:
   #   print "returning smaller of %r" % smaller
        return smaller
    if larger % smaller == 0:
        return smaller
    else:
        larger = larger % smaller
        return gcdRecur(smaller, larger)
gcdRecur(12,144)
"""
# MIT version
def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)


