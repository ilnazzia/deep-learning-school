def cumsum_and_erase(a, erase=1):
    B = [sum(a[:i]) for i in range(1, len(a) + 1) if sum(a[:i]) != erase]
    return B

A = [5, 1, 4, 5, 14] 
print(cumsum_and_erase(A, erase=10))
# [5, 6, 15, 29]