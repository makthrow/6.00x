"""
You observe that the probability of
first seeing a 1 on the n-th roll decreases
as n increases. You would like to know the 
smallest number of rolls such that this probability
is less than some limit. Complete the Python procedure,
probTest, to compute this.
"""

def probTest(limit):
    rolls = 0
    probability = 1

    # nth roll: probability is (5/6 * n-1) * 1/6
    while probability > limit:

        rolls += 1
        # compute probability for nth roll 
        if rolls == 1:
            probability = 1.0/6.0
        else:
            probability = ((5.0/6.0) **(rolls -1)) * (1.0/6.0)

     #   print rolls, probability
        
    return rolls 

        

