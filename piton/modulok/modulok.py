def szamitkerulet(aOldal, cOldal, bOldal):
    return aOldal + bOldal + cOldal

def szamitterulet(alap,magassag):
    return (alap*magassag)/2

if __name__ == "__main__":
    print(szamitkerulet(10,15,20))
    print(szamitterulet(10,20))