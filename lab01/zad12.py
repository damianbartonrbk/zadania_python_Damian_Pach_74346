a = float(input("Podaj wartość liczby a: "))
b = float(input("Podaj wartość liczby b: "))
c = float(input("Podaj wartość liczby c: "))

def funkcja_a(a):
    if a > 0:
        return 2 * a
    elif a == 0:
        return 0
    else:
        return -3 * a

def funkcja_b(b):
    if b >= 1:
        return b**3
    else:
        return b

def funkcja_c(c):
    if c > 2:
        return 2 + c
    elif c == 2:
        return 8
    else: 
        return c - 4


print ("Wynik działania a to: ", funkcja_a(a))
print ("Wynik działania b to: ", funkcja_b(b))
print ("Wynik działania c to: ", funkcja_c(c))