a = int(input("Adj meg egy számot! "))
b = int(input("Adj meg egy másik számot! "))

if a == b:
    print("A két szám egyenlő")
elif b < a:
    print("A nagyobb érték",a)
else:
    print("A nagyobb érték",b)