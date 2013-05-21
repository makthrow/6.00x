import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    yes = 0
    for trial in range(numTrials):
        yes += pickThreeBalls()
        #print yes
    return yes/float(numTrials)



def pickThreeBalls():
    ballDic = {'red': 3, 'green': 3}

    # pick 3 balls out
    for i in range(3):
            totalBalls = ballDic['red'] + ballDic['green']

            #print "red/green = %r / %r,   = %r" % (ballDic['red'] , ballDic['green'] , ballDic['red'] * 1.0 / totalBalls)
            
            if random.random() < (ballDic['red'] * 1.0) / totalBalls:
                  
                   ballDic['red'] -= 1
            else:
                   ballDic['green'] -= 1 
        

            #print ballDic
    if ballDic['red'] == 0 or ballDic['green'] == 0:
            #print "success"
            return 1
    return 0
