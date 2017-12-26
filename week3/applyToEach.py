# Applies a function to each value in a list, and returns the new values

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    print(L)

# 1. Prints absolute value of each item in list
#applyToEach(testList, abs)


# 2. Prints each item in the list +1
def plusOne(number):
    return number + 1

#applyToEach(testList, inc)


# 3. Prints each item in the list squared
def squared(number):
    return number**2

#applyToEach(testList, squared)