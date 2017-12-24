# Returns the remaining balance at the end of each month, if the minimum amount is payed.

balance = 42
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
monthlyPaymentRate = 0.04

for month in range(0, 12):
    payment = balance * monthlyPaymentRate
    balanceRemaining = balance - payment
    balance = balanceRemaining + (balanceRemaining * monthlyInterestRate)

print("Remaining balance: " + str(round(balance, 2)))