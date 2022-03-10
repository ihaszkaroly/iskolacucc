
def fug():
    a = input("Adja meg a vizsgázó nevét: ")
    i = True
    c = len(a)
    while c > 0:
        b = int(input("Adja meg a vizsgázó pontszámát: "))
        if b >= 48:
            i = True
        else:
            i = False
        if i == True:
            print(a,"vizsgája sikeres.")
        else:
            print(a,"vizsgája sikertelen.")
        a = input("Adja meg a vizsgázó nevét: ")
        c = len(a)
fug()