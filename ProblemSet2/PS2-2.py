balance = 4773
annualInterestRate = 0.2
# result code should generate: Lowest Payment: 360


# Variables:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# The monthly payment must be a multiple of $10 and is the same for all months
# TODO: CALCULATE MONTHLY PAYMENT BASED ON INITIAL BALANCE

""" MATHS:
Monthly interest rate = (Annual interest rate) / 12
Updated balance each month = (Previous balance - Minimum monthly payment) x (1 + Monthly interest rate)
"""

monthlyInterestRate = annualInterestRate / 12
fixedMonthlyPayment = 0
updatedBalance = balance

def remainingBalance(fixedMonthlyPayment):
    month = 1
    updatedBalance = balance
    while month <= 12:
        updatedBalance = round((updatedBalance - fixedMonthlyPayment) * (1 + monthlyInterestRate), 2)
        month += 1
    return updatedBalance

def balancePaidInFull(updatedBalance):
    return updatedBalance <= 0

while not balancePaidInFull(updatedBalance):
    fixedMonthlyPayment += 10
    updatedBalance = remainingBalance(fixedMonthlyPayment)
    

print "Lowest Payment: %r" % fixedMonthlyPayment
                     
