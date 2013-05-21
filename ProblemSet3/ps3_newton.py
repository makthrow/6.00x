# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.

    poly: list of numbers, length > 0
    x: number
    returns: float
    '''

    indexValue = 0
    total = 0.0
    power = 0 # count the index. this is the power
    for c in poly:
        total += c * (x ** power)
        power += 1

    return total




# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].

    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''

    """
    example case:
    - 13.39 + 17.5x^2 + 3x^3 + x^4
    poly = [-13.39, 0.0, 17.5, 3.0, 1.0]
    print computeDeriv(poly)
    [0.0, 35.0, 9.0, 4.0] # 35x + 9x^2 + 4x^3
    """
    # FILL IN YOUR CODE HERE...

    # poly value. muliply by its power
    # then put in a new list, omit first poly value
    power = 0.0 # count the index. this is the power. omit first value
    derivList = []
    if len(poly) == 1:
     #   print "length poly is 0"
        derivList.append(0.0)
        return derivList


    else:
        for c in poly:
            value = c * power
            power += 1
            derivList.append(value)

    derivList.pop(0)
    return derivList

# Problem 3: Newton's Method

def computeRoot(poly, x_0, epsilon):

    iter = 0
    rootiter = [] # return list
    # calculate x0
    calcguess = evaluatePoly(poly, x_0)
    #print "calcguess: %r " % calcguess

    while abs(calcguess) > epsilon:
    # use recursion call to calculate x1
        iter += 1
     #   print "iter: %r" % iter
     #   print "x_0: %r" % x_0
        x_0 = x_0 - (evaluatePoly(poly, x_0) / evaluatePoly(computeDeriv(poly), x_0))
        calcguess = evaluatePoly(poly, x_0)
    rootiter.append(x_0)
    rootiter.append(iter)
    return rootiter

print computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1,  .0001)
print computeRoot([1, 9, 8], -3, .01)
print computeRoot([1, -1, 1, -1], 2, .001)
print evaluatePoly(computeDeriv([1, 9, 8]),2)

"""
def computeRoot(poly, x_0, epsilon):

    iter = 0
    x1 = 0
    rootiter = []
    # calculate x0
    calcguess = evaluatePoly(poly, x_0)
    if calcguess < epsilon:
         rootiter.append(calcguess)
         rootiter.append(iter)
         return rootiter
    else: # use recursion call to calculate x1
        x1 = x_0 - evaluatePoly(poly, x_0) / evaluatePoly(computeDeriv(poly), x_0)
        computeRoot(poly, x1, epsilon)
    #returns: list [float, int]
    return
"""

