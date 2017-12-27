# Returns a list of keys in aDict that pay to integer values that are unique

def uniqueValues(aDict):
    
    newDict = {}
    keys = []

    for key in aDict:
        value = aDict[key]
        newDict = aDict.copy()
        del newDict[key]
        hasDuplicate = False

        for key2 in newDict:
            if newDict[key2] == aDict[key]:
                hasDuplicate = True
        
        if hasDuplicate == False:
            keys.append(key)

    keys.sort()
    return keys

print(uniqueValues({8: 1, 0: 4, 1: 1, 5: 2, 9: 4}))