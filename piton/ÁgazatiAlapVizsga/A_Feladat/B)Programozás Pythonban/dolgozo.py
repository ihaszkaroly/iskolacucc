#Ihász Károly 2021-12-08
print("Ihász Károly 2021-12-08")
def dolgozok():
    f = open("feherBt.txt" , "r" ,encoding="utf-8")
    r = f.readline()
    c = -1
    while(r):
        r = f.readline()
        if(len(r) != 0):
            c += 1
    f.close()
    print("Dolgozók száma:",c)
def nyiregy():
    f = open("feherBt.txt" , "r" ,encoding="utf-8")
    r = f.readline()
    a = 0
    while(r):
        r = f.readline()
        if(len(r) != 0):
            h = r.split(":")
            if h[1] == "Nyíregyháza":
                a += 1
    f.close()
    print("Nyíregyházi dolgozók száma:",a)
def gyorfiz():
    f = open("feherBt.txt" , "r" ,encoding="utf-8")
    r = f.readline()
    c = -1
    i = 0
    while(r):
        r = f.readline()
        if(len(r) != 0):
            c += 1
            h = r.split(":")
            i = i+int(h[3])
    i = i/c
    print("Győri dolgozók átlag fizetésének átlaga: %.2f"%i)


dolgozok()
nyiregy()
gyorfiz()