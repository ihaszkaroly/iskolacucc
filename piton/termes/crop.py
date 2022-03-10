from cropModell import CropModell
from typing import List

class Crop:
    def __init__(self):
        self.separator = ("----------------------------------------")
        self.file_name = "termes.txt"
        self.termesek: List[CropModell] = []
    def read(self):
        fp = open(self.file_name,"r",encoding="utf-8")
        self.sorok = fp.readlines()
        fp.close()
    def convert(self):
        for sor in self.sorok[1::]:
           (id,name,area,size,height,year) = sor.split(":")
           termes = CropModell(int(id),name,area,int(size),float(height.replace(",",".")),int(year))
           self.termesek.append(termes)
    def hany_tonn_buz(self):
        buza = 0
        for termes in self.termesek:
            if termes.name == "búza":
                buza += termes.height
        print(buza)
    def haromszaznaltobb(self):
        print(self.separator)
        for termes in self.termesek:
            if termes.height > 300:
                print(termes.name,termes.height)
    def hanyarpa(self):
        print(self.separator)
        arpa = 0
        for termes in self.termesek:
            if termes.name == "árpa":
                arpa += 1
        print("Ennyi területen terem árpa:",arpa)
    def tobbmint80hektar(self):
        print(self.separator)
        a = 0
        for termes in self.termesek:
            if termes.size > 80:
                a += 1
        print("Ennyi 80 hektárnál nagyobb terület van:",a)
    def milyengabonacsendesen(self):
        print(self.separator)
        for termes in self.termesek:
            if termes.area == "Csendes":
                print("Ez terem Csendesen:",termes.name)
    def legkevesebbbuza(self):
        tempList: List[CropModell] = []
        for termes in self.termesek:
                if termes.name == "búza":
                    tempList.append(termes)
        buza = tempList[0]
        for termes in tempList[1::]:
            if termes.height < buza.height:
                buza = termes
        print(buza.area)


crop = Crop()
crop.read()
crop.convert()
crop.hany_tonn_buz()
crop.haromszaznaltobb()
crop.hanyarpa()
crop.tobbmint80hektar()
crop.milyengabonacsendesen()
crop.legkevesebbbuza()