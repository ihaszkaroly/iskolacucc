a = ["Budapest","Miskolc","Pécs","Zalaegerszeg"]
b = input("Adjon meg egy pálya területet: ")
for i in range(0,4):
    if a[i] == b:
        c = int(input("Adja meg az öregedési időt években: "))
        if( c > 2 and c < 6):
            print("felülvizsgálatot igényel")
        elif c > 5:
            print("sürgős karbantartás")
        else:
            print("Normál")