def cw():
    f = open("feherBt.txt" , "r" ,encoding="utf-8")
    r = f.readline()
    c = 0
    while(r):
        r = f.readline()
        if(len(r) != 0):
            c += 1
    print(c)

def getcity():
    f = open("feherBt.txt" , "r" ,encoding="utf-8")
    r = f.readline()
    while(r):
        r = f.readline()
        if(len(r) != 0):
            rSpt = r.split(":")
            print(rSpt[1])


def start():
    cw()
    getcity()

start()

