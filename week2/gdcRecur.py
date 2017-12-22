# Finds the greatest common denominator between 2 numbers, recursively

def gdcRecur(a, b):
    smallest = min([a, b]);
    largest = max([a, b]);

    if largest % smallest == 0 and smallest % smallest == 0:
        return smallest;  
    else:
        return gdcRecur(b, a % b);

print(gdcRecur(55, 90));