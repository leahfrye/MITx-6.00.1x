# Using a generator, returns a sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11

def genPrimes():
    next = 2

    while next > 1:
        isPrime = True
        for i in range(2, next):
            if next % i == 0:
                next += 1
                isPrime = False
                break
        
        if isPrime:
            yield next
            next += 1

prime = genPrimes();
print(prime.__next__())
print(prime.__next__())
print(prime.__next__())
print(prime.__next__())
print(prime.__next__())
print(prime.__next__())
print(prime.__next__())
print(prime.__next__())
print(prime.__next__())
print(prime.__next__())
print(prime.__next__())

