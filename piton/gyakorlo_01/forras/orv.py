import paciens

class Orv:
    def beolvas(self):
        fajlnev = 'páciens.txt'
        fajlmod = 'r'
        fp = open(fajlnev, fajlmod)
        sorok = fp.readlines()
        fp.close()
        self.paciensek = []
        for sor in sorok:
            (nev, tunet, kezeles, ido, ar) = sor.split(':')
            paciens = Paciens(nev, tunet, kezeles, ido, ar)
            paciensek.append(paciens)
    
    def moxavalKezeltek(self):
        if self.kezeles == "moxa":
            print(self.nev)

    def bevetel(self):
        for i in range(0,5):
            self.ar += ar
        print(self.ar)

    def tizezernelNagyobbBevetel(self):
        for i in range(0 , 5):
            if ar > 10000:
                print(nev,tunet,kezeles,ido,ar)