# Calculates base by using successive multiplication
def iterPower(base, exp):
    count = 1;
    total = base;
    while count < exp:
        total = total * base;
        count += 1;
    return total;

print(iterPower(7.74, 10));