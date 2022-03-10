from lenbt2 import Valami
class Bt:
    def beolvas(self):
        file = open("lentbt.txt","r",encoding="utf-8")
        sorok = file.readlines()
        file.close()
        self.dolgozok = []
        for sor in sorok:
            (sorszam,nev,telepules,cim,fizetes,szul) = sor.split(":")
            dolgozo = Valami(sorszam,nev,telepules,cim,int(fizetes),szul)
            self.dolgozok.append(dolgozo)
    def fizetes(self):
        a = 0
        b = 2000000
        for dolgozo in self.dolgozok:
            if dolgozo.fizetes > b:
                a += 1
        print(a,"dolgozó fizetése több mint 2.000.000")

bt = Bt()
bt.beolvas()
bt.fizetes()
