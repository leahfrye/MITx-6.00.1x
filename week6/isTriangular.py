def is_triangular(k):
    num = 0
    if k == 1:
        return True
    for i in range(k + 1):
        if num == k:
            return True
        num += i
    return False

print(is_triangular(91))