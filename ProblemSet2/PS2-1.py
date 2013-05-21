updatedBalance = balance
monthlyInterestRate = annualInterestRate / 12
totalPaid = 0
month = 1
while month <= 12:
    minMonthlyPayment = round(monthlyPaymentRate * updatedBalance, 2)
    updatedBalance = round((updatedBalance - minMonthlyPayment) * (1 + monthlyInterestRate), 2)
    print "Month: %d" % month
    print "Minimum monthly payment: %r" % minMonthlyPayment
    print "Remaining balance: %r" % updatedBalance
    month += 1
    totalPaid += minMonthlyPayment
print "Total paid: %r" % round(totalPaid,2)
print "Remaining balance: %r" % updatedBalance
