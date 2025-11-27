a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

start = min(a, b)
koniec = max(a, b)

i = start
while i <= koniec:
    if i % 2 != 0:
        i = i + 1
        continue
    print(i)
    i = i + 1