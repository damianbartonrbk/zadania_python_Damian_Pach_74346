a = float(input("Podaj pierwszą wartość: "))
b = float(input("Podaj drugą wartość: "))

operacja = int(input("Jaką operację chcesz wykonać z pośród dodawanie-1/dzielenie-2/mnożenie-3/odejmowanie-4: "))
if operacja == 1:
    dodawanie = a + b
    print ("Wynik dodawania to: ", dodawanie)
elif operacja == 3:
    mnożenie = a*b
    print ("Wynik mnożenia to: ", mnożenie)
elif operacja == 4:
    odejmowanie = a-b
    print ("Wynik odejmowania to: ", odejmowanie)
elif operacja == 2:
    if b == 0:
        print ("Nie dziel przez 0!")
    else:
        dzielenie = a/b
        print ("Wynik dzielenia to: ", dzielenie)