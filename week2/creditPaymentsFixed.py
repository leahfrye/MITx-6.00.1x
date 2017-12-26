# Returns the minimum monthly payment required to pay off the balance in a year, using increments of 10


def findMinPayment(balance, annualInterestRate, minPayment):
    monthlyInterestRate = annualInterestRate/12
    balanceRemaining = balance

    for month in range(0, 12):
        balanceRemaining -= minPayment
        balanceRemaining += balanceRemaining * monthlyInterestRate

    if balanceRemaining > 0:
        findMinPayment(balance, annualInterestRate, minPayment + 10)
    
    else:
        print("Lowest monthly payment: " +  str(minPayment))


findMinPayment(3329, 0.2, 10)
