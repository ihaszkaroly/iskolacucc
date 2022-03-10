from dolgozo import dolgozo


class talon:
    def __init__(self):
        self.filename = "talonkft.txt"
        self.dolgozo = []
    def open_file(self):
        fp = open(self.filename, "r",encoding="utf-8")
        lines = fp.readline()
        for line in lines:
            line = line.strip()
            (nev , telepules, cim ,szulnap, fizetes) = line.split(":")
            self.dolgozo.append()
            print(nev)
        fp.close()
    def kitataidolgozo(self):
        for dolgozo in self.dolgozo:
            if dolgozo.telepules == "Tata":
                print(dolgozo.nev,dolgozo.telepules)
            


Talon = talon()
talon.open_file()
talon.kitataidolgozo()
