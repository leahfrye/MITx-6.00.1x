# Return a new list of strings less than 4 characters long

def lessThan4(list):
    newList = []
    
    for item in list:
        if len(item) < 4:
            newList.append(item)

    return newList

print(lessThan4(["apple", "cat", "dog", "banana"]))