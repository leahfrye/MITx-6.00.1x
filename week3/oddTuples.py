# Takes a tuple as an input and returns a new tuple, where every other element of the input

def oddTuples(aTup):
    oddTups = ()
    count = 0
    for x in aTup:
        if count % 2 == 0:
            oddTups += (x,)
        count += 1
    print(oddTups)

oddTuples((4, 5, 18, 10, 7, 1, 8, 15, 4, 8))