class dolgozo:
    def __init__(self):
        self.nev = "névtelen"
        self.telepules = "ismeretlen"
        self.fizetes = 0
    def allitnev(self, atvettnev):
        self.nev = atvettnev
    def kernev(self):
        return self.nev
class mernok(dolgozo):
    def __init__(self):
        self.diploma = "ismeretlen"

kati = mernok()
kati.allitnev("Latner Katalin")
kati.diploma = "ASDA-846464"
print(kati.diploma)