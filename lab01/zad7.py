import random

ilosc_km = random.randint(0, 200)
srednie_spalanie = float(input("Podaj spalanie na 100KM: "))
cena_paliwa = float(input("Podaj cene paliwa: "))

zuzyte_paliwo = ilosc_km * (srednie_spalanie / 100)
koszt_podrozy = zuzyte_paliwo * cena_paliwa

print (f"Na {ilosc_km} KM zostało zużytych", round(zuzyte_paliwo, 2), "litrów paliwa.")
print (f"Koszt podróży wyniósł", round(koszt_podrozy, 2), "PLN.")
