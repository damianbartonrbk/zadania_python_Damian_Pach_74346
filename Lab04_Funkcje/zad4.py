def bmi(waga, wzrost):
    wynik = waga / (wzrost * wzrost)
    if wynik < 18.5:
        print("BMI:", wynik, "- niedowaga")
    elif wynik < 25:
        print("BMI:", wynik, "- waga prawidłowa")
    elif wynik < 30:
        print("BMI:", wynik, "- nadwaga")
    else:
        print("BMI:", wynik, "- otyłość")
bmi(80, 1.8)