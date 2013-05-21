def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if x == 1:
        return 0
    exp = 0
    while b ** exp < x:
        exp += 1
    # going to overshoot exp by 1 in the while loop when it exits
    # so return exp - 1
    if b ** exp > x:
       return exp - 1
    return exp



