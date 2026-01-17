rachunki = {
    "wrzesien": 210,
    "październik": 240,
    "listopad": 190,
    "grudzien": 260
}
wartosci = list(rachunki.values())
maks = max(wartosci)
mini = min(wartosci)
suma = sum(wartosci)
srednia = suma / len(wartosci)
print("Maks:", maks)
print("Min:", mini)
print("Suma:", suma)
print("Średnia:", srednia)
ostatni_miesiac = list(rachunki.keys())[-1]
ostatnia_wartosc = rachunki[ostatni_miesiac]
if ostatnia_wartosc > srednia:
    print("Trzeba zacisnąć pasa")
else:
    print("Wszystko okay")

