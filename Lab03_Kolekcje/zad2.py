a = str(input("Podaj jakieś zdanie: "))
b = list(a)
c = sorted(b)
print("Posortowane zdanie: ", c)
alfabet = list("aąbcćdeęfghijklłmnńoprsśtuvwxyzźż")
brakujace = []
for i in alfabet:
    if i not in a.lower():
        brakujace.append(i)
print("Brakujące litery alfabetu w podanym zdaniu to: ", brakujace)

nieparzyste = c[1::2]
for i2 in nieparzyste:
    c.remove(i2)
print("Lista bez nieparzystych indexów: ", c)

b2 = a.split()
nowe_slowa = []
for i3 in b2:
    pierwsza = i3[0].lower()
    ostatnia = i3[-1].upper()
    srodek = i3[1:-1]
    nowe_slowa.append(pierwsza + srodek + ostatnia)

nowe_zdanie = " ".join(nowe_slowa)
print("c)", nowe_zdanie)

najdluzsze = max(b2)
print("Najdłuższe słowo to: ", najdluzsze)