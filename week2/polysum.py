# Sums the area and square of a perimeter and returns it

# n = number of sides
# s = length of each side

import math;

def polysum(n, s):
    area = (0.25*n*s**2)/math.tan(math.pi/n);
    perimeter = n * s;
    return round(area + (perimeter**2), 4);

print(polysum(59, 4));