import math

a = int(input("podaj pierwszą liczbę: "))
b = int(input("podaj drugą liczbę: "))
c = int(input("podaj trzecią liczbę: "))
delta = b**2-4*a*c
if(delta > 0):
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("x1 =", x1)
    print("x2 =", x2)

elif(delta == 0):
    x0 = -b/(2*a)
    print ("x0 = ", x0)

elif(delta < 0):
    print ("delta jest ujemna, brak rozwiązań")
