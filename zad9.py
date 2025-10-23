a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

dodawanie = a + b
odejmowanie = a - b
mnozenie = a*b
potegowanie = a**b

print (f"Wynik dodawanie tych dwóch liczb to: {dodawanie}")
print (f"Wynik odejmowania tych dwóch liczb to: {odejmowanie}")
print (f"Wynik mnożenia tych dwóch liczb to: {mnozenie}")
print (f"Wynik potęgowania tych dwóch liczb to: {potegowanie}")
if(b == 0):
    print ("Nie można dzielić przez 0!")
else:
    dzielenie = a/b
    print (f"Wynik dzielenia tych dwóch liczb to: {dzielenie}")