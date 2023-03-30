def almost_double_factorial(n):
    result = 1
    if n == 0:
        return result
    elif n >= 1:
        for i in range(1, n + 1):
            if i % 2 == 1:
                result *= i
    return result

print(f"fuctorial = {almost_double_factorial(6)}")