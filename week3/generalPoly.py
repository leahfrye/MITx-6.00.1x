
def general_poly(L):

    def calculate(numToMultiply):
        count = len(L) - 1
        total = 0
        
        for int in L:
            total += int * numToMultiply**count
            count -= 1

        return total

    return calculate

print(general_poly([1, 2, 3, 4])(10))