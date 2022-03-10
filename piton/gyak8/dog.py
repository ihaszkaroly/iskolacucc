from math import radians


fajta = input("Kutyafajta: ")
def havedog(fajta):
    kutya = ["dalmata","agár","terrier","kuvasz"]
    if fajta in kutya:
        return True
    else:
        return False
while fajta != "vege":
    if fajta != "vege":
        havedog(fajta)
        if havedog(fajta):
            print("Van ilyen fajta.")
        else:
            print("Jelenleg nincs ilyen fajta")
    fajta = input("Kutyafajta: ")