from re import I
from jurta2 import JurtaM
from typing import List
class Jurta():
    def __init__(self):
        self.separator = ("----------------------------------------")
        self.file_name = "jurtabt.txt"
        self.dolgozok: List[JurtaM] = []
    def read(self):
        fp = open(self.file_name,"r",encoding="utf-8")
        self.sorok = fp.readlines()
        fp.close()
    def convert(self):
        for sor in self.sorok[1::]:
           (nev,telepules,cim,szul,fiz) = sor.split("#")
           dolgozo = JurtaM(nev,telepules,cim,szul,int(fiz))
           self.dolgozok.append(dolgozo)
    def miskolcfiz(self):
        print(self.separator)
        fiz = 0
        for dolgozo in self.dolgozok:
            if dolgozo.telepules == "Miskolc":
                fiz += dolgozo.fiz
        print("Miskolciak össz fizetése:",fiz)
    def hatvanlegnagyobbfiz(self):
        print(self.separator)
        i = 0
        for dolgozo in self.dolgozok:
            if dolgozo.telepules == "Hatvan":
                if dolgozo.fiz > i :
                    i = dolgozo.fiz
        print("Hatvanban a legnagyobb fizetés:",i)
    def hanybudapest(self):
        print(self.separator)
        i = 0
        for dolgozo in self.dolgozok:
            if dolgozo.telepules == "Budapest":
                i += 1
        print(i,"Dolgozó van Budapestről.")
        print(self.separator)


jurta = Jurta()
jurta.read()
jurta.convert()
jurta.miskolcfiz()
jurta.hatvanlegnagyobbfiz()
jurta.hanybudapest()