# Finds the greatest common denominator between 2 numbers, recursively

def isIn(char, aStr):
    
    if char == aStr:
        return True;

    elif len(aStr) >= 1:
        middleChar = aStr[round((len(aStr) - 1)/2) - 1];
        if char == middleChar:
            return True;
        if char > middleChar:
            return isIn(char, aStr[aStr.index(middleChar) + 1: len(aStr)]);
        elif char < middleChar:
            return isIn(char, aStr[0: aStr.index(middleChar)]);
    else:
        return False;
      
print(isIn("e", "cejs"));