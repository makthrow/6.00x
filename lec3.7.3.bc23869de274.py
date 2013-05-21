# Lecture 3.7, slide 3

# Newton-Raphson for square root

epsilon = 0.01
y = 12345
guess = y/2.0
guess_counter = 0

while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y)/(2*guess))
    guess_counter += 1
    print "Guess %d: %f" % (guess_counter, guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))
