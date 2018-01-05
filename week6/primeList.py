def primes_list(N):
    list = []
    
    for i in range(2, abs(N) + 1):
        if i == 1:
            list.append(i)
        else:
            isPrime = True
            for j in range(2, i):
                if i % j == 0:
                    isPrime = False
                    break

            if isPrime:
                list.append(i)
    return list

print(primes_list(100))