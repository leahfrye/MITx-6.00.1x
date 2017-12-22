# Finds the greatest common denominator between 2 numbers, iteratively

def gdcIter(a, b):
    smallest = min([a, b]);
    largest = max([a, b]);

    x = smallest;

    while x > 0:
        if largest % x == 0 and smallest % x == 0:
            return x;  
        else:
            x -= 1;


print(gdcIter(70, 100));