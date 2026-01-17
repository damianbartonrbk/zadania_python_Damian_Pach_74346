def potega(a, n):
    if n == 0:
        return 1
    return a * potega(a, n - 1)
print(potega(2, 5))