# class macsek:
#     nev = "névtelen"
#     kor = 0
#     def hang(self):
#         print("miau")
#         print(self.nev + " vagyok")
#     def allitkor(self, atvettkor):
#         self.kor = atvettkor

# cirmi = macsek()
# cirmi.kor = 5
# cirmi.nev = "cirmi"
# print(cirmi.kor,cirmi.nev)
# cirmi.hang()
# cirmi.allitkor(8)
# print(cirmi.kor)

class Tamas:
    def __init__(self):
        self.nev = "Névtelen"
        self.kor = 0
        self.eletero = 20
    def alliteletero(self, eletero):
        self.eletero = eletero

pad = Tamas()

adat = ""
while adat != "vege":
    adat = input("Adatot kérek: ")
    pad.alliteletero(pad.eletero - 1)
    if adat == "etet":
        pad.alliteletero(pad.eletero +10)
    if pad.eletero < 10:
        print("etess")
    if pad.eletero < 1:
        print("meghaltam")
        quit()
    

    