def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if f(guess) - guess < epsilon:
            print guess
            return guess
        else:
            guess = f(guess)
            print guess
            
    return guess

def f(guess):
    guess /= 2
    return guess
