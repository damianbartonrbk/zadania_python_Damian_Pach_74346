print("a)")
n = int(input("Podaj liczbę wierszy: "))
for i in range(n):
    print("* * *")

print("b)")
n2 = int(input("Podaj liczbę wierszy: "))
for i2 in range(1, n2 + 1):
    print("* " * i2)

print("c)")
n3 = int(input("Podaj liczbę wierszy: "))
for i3 in range(1, n3 + 1):
    print(" " * (n3 - i3) + "* " * i3)