bilet = 20
biletS = 20 * 3/4
bilet4do18 = 10
bilet0do4 = 0



wiek = int(input("Podaj swój wiek "))

if wiek < 4 and wiek > 0:
    print (f"Cena twojego biletu wynosi: {bilet0do4}")
elif wiek < 18 and wiek > 4:
    print (f"Cena twojego biletu wynosi: {bilet4do18}")
elif wiek >= 18:
    status = str(input("Czy jestes stundentem? "))
    if status == "Tak" or status == "tak":
        print (f"Cena twojego biletu wynosi: {biletS}")
    else:
        print (f"Cena twojego biletu wynosi: {bilet}")




