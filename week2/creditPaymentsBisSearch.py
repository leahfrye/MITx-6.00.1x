# Returns the minimum monthly payment required to pay off the balance in a year, using bisection search

def findMinPayment(balance, annualInterestRate, lowerBound, upperBound):
    monthlyInterestRate = annualInterestRate/12
    balanceRemaining = balance
    payment = (upperBound + lowerBound)/2

    for month in range(0, 12):
        balanceRemaining -= payment
        balanceRemaining += balanceRemaining * monthlyInterestRate    

    if round(balanceRemaining, 2) < -1:
        findMinPayment(balance, annualInterestRate, lowerBound, payment - 1)

    elif round(balanceRemaining, 2) > 1:
        findMinPayment(balance, annualInterestRate, payment + 1, upperBound)

    else:
        print("Lowest Payment: " + str(round(payment, 2)))

balance = 999999
annualInterestRate = 0.18
lowerBound = balance/12
upperBound = round((balance * ((1 + annualInterestRate/12)**12))/12, 2)

findMinPayment(balance, annualInterestRate, lowerBound, upperBound)
