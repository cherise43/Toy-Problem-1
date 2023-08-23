def two_positive(a, b, c):
    positives = [num for num in [a, b, c] if num > 0]
    return len(positives) == 2


print(two_positive(2, 4, -3))  
print(two_positive(-4, 6, 8))  


