"""
Monthly interest rate = (Annual interest rate) / 12
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12
"""

#Test Case 1:
balance = 320000
annualInterestRate = 0.2
# Lowest Payment: 29157.09

monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
updatedBalance = balance

def remainingBalance(fixedMonthlyPayment):
    updatedBalance = balance
    month = 1
    while month <= 12:
        updatedBalance = (updatedBalance - fixedMonthlyPayment) * (1 + monthlyInterestRate)
        month += 1
    return updatedBalance

def balancePaidInFull(updatedBalance):
    return updatedBalance <= 0

def binarySortToLowerBound():
    global lowerBound
    global upperBound

    epsilon = 0.01
    
    while abs(upperBound - lowerBound) > epsilon:
        fixedMonthlyPayment = (lowerBound + upperBound) / 2
        updatedBalance = remainingBalance(fixedMonthlyPayment)
        if updatedBalance == 0:
            return fixedMonthlyPayment
    
        if updatedBalance > 0:
            lowerBound = fixedMonthlyPayment
        else:
            upperBound = fixedMonthlyPayment
        print (upperBound - fixedMonthlyPayment)

    print "lowerBound: %f" % lowerBound
    return lowerBound

fixedMonthlyPayment = binarySortToLowerBound()

while not balancePaidInFull(updatedBalance):
    fixedMonthlyPayment += 0.01
    updatedBalance = remainingBalance(fixedMonthlyPayment)
        
#print updatedBalance
#print remainingBalance(29157.09)
print "Lowest Payment: %.2f" % fixedMonthlyPayment                    
