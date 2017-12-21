# Calculates base recursively

def recurPower(base, exp):
    if exp == 1:
        return base;
    elif exp <= 0:
        return 1.0000;
    else:
        return base * recurPower(base, exp - 1);

print(recurPower(-8.55, 0));