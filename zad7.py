a = float(input("Podaj a: "))
b = float(input("Podaj b:"))
if(a == 0):
    if(b == 0):
        print("Równanie tożsamościowe")
    else:
        print("Równanie sprzeczne")
else:
    x = -b/a
    print (f"x jest równy {x}")

    
