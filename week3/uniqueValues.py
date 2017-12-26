# Returns a list of keys in aDict that pay to integer values that are unique

def uniqueValues(aDict):
    
    newDict = {}
    keys = []

    for key,value in aDict:
        if value not in newDict.values() and type(value) == int:
            keys.append(key)
        else:
            keys.remove(key)
    print(newDict)
    
    keys.sort()
    return keys

print(uniqueValues({1: 1, 2: 2, 3: 2, 4: "cat"}));