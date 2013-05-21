def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    def sumNuggets(box6, box9, box20):
        return ((box6 * 6) + (box9 * 9) + (box20 * 20))


        
    #eg.  41 works (20, 9, 6, 6,)

    if n % 6 == 0 or n % 9 == 0 or n % 20 == 0:
        return True
    if n < 6:
        return False
    box6 = 0
    box9 = 0
    box20 = 0
    totalNuggets = sumNuggets(box6, box9, box20)
    totalBoxes = box6 + box9 + box20

    while totalNuggets != n:
        if totalNuggets > n:
            break
        
        for i in range(n/6 + 6):

            totalNuggets = sumNuggets(box6, box9, box20)
            print "box6: %r, box9: %r, box20: %r, total: %r" % (box6,box9,box20,totalNuggets)
            if totalNuggets == n:
                return True
            elif totalNuggets > n:
                break

            for i in range(n/9 + 9):

                totalNuggets = sumNuggets(box6, box9, box20)
                print "box6: %r, box9: %r, box20: %r, total: %r" % (box6,box9,box20,totalNuggets)
                if totalNuggets == n:
                    return True
                elif totalNuggets > n:
                    break
            

                for i in range(n/20 + 20):

                    totalNuggets = sumNuggets(box6, box9, box20)
                    print "box6: %r, box9: %r, box20: %r, total: %r" % (box6,box9,box20,totalNuggets)
                    if totalNuggets == n:
                        return True
                    elif totalNuggets > n:
                        break
                    box20 += 1

                box20 = 0
                
                box9 += 1
            box9 = 0  
    
            box6 += 1
    
    return False
        
