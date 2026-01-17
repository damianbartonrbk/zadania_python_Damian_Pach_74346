def pole_trojkata(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Błędne dane"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Nie da się zbudować trójkąta"
    p = (a + b + c) / 2
    pole = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return pole
print(pole_trojkata(3, 4, 5))