from dolgozo import Dolgozo

class Latbt:
    def olvas_fajl(self):
        fp = open("latbt.txt", "r", encoding="utf-8")
        lines = fp.readlines()
        fp.close

        self.dolgozok = []
        for line in lines:
            (nev, telepules, fizetes) = line.split(':')
            dolgozo = Dolgozo(nev, telepules, fizetes)
            self.dolgozok.append(dolgozo)

        def szamitAtlag(self):
            pass

        def kiirTelepulesek(self):
            pass

        def kiirFajlba(self):
            fp = open('adat')

            fp.close()

        

