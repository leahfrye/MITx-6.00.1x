# Finds the greatest common divisor between two positive integers

def gdc(a, b):

    if b == 0:
        return a
    else:
        return gdc(b, a % b)

print(gdc(56.6, 6.3))