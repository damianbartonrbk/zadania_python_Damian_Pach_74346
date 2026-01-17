n = int(input("Podaj n: "))
x = int(input("Podaj x: "))
lista = []
for i in range(n):
    tekst = input("Podaj napis: ")
    lista.append(tekst)
krotka = tuple(lista)
ilosc_znakow = 0
for element in krotka:
    ilosc_znakow += len(element)
print("Ilość znaków:", ilosc_znakow)
licznik_k = 0
for element in krotka:
    licznik_k += element.count("k")
print("Ilość liter 'k':", licznik_k)
licznik_kt = 0
for element in krotka:
    if "kt" in element:
        licznik_kt += 1
print("Ilość ciągów zawierających 'kt':", licznik_kt)
s = int(input("Podaj s: "))
licznik_dluzsze = 0
for element in krotka:
    if len(element) > s:
        licznik_dluzsze += 1
print("Ilość ciągów dłuższych niż s:", licznik_dluzsze)