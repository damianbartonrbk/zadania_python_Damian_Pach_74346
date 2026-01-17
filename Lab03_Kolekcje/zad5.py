zakupy = {}
n = int(input("Ile produktów chcesz dodać: "))
for i in range(n):
    nazwa = input("Podaj nazwę produktu: ")
    cena = float(input("Podaj cenę: "))
    zakupy[nazwa] = cena
print(zakupy)
suma = 0
for cena in zakupy.values():
    suma += cena
print("Suma wydatków:", suma)