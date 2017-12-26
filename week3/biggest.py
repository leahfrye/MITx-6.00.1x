# Returns the key with the largest number of values associated with it

def biggest(dict):
    count = 0;
    biggest = ''
    for i in dict:
        if count == 0:
            count = len(dict[i])
            biggest = i
        elif len(dict[i]) > count:
            count = len(dict[i])
            biggest = i
    return biggest

print(biggest({'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]}))
