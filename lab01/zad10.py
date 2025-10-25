x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj drugą liczbę: "))
z = float(input("Podaj trzecią liczbę: "))

# xyz, xzy, zxy, zyx, yzx, yxz

if x < y and y < z:
    print(f"kolejność liczb od najmniejszej do największej to: {x} {y} {z}")
elif x < z and z < y:
    print(f"kolejność liczb od najmniejszej do największej to: {x} {z} {y}")
elif z < x and x < y:
    print(f"kolejność liczb od najmniejszej do największej to: {z} {x} {y}")
elif z < y and y < x:
    print(f"kolejność liczb od najmniejszej do największej to: {z} {y} {x}")
elif y < z and z < x:
    print(f"kolejność liczb od najmniejszej do największej to: {y} {z} {x}")
elif y < x and x < z:
    print(f"kolejność liczb od najmniejszej do największej to: {y} {x} {z}")