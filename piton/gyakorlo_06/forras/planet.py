def check_planet(bolyesz):
    torp = ["Ceres","Haumea","Plútó","Makemake","Eris"]
    bolygo = ["Vénusz","Mars","Jupiter","Szaturnusz","Uránusz","Neptunusz"]
    if bolyesz in torp:
        return "Törpebolygó"
    elif bolyesz in bolygo:
        return "Bolygó"
    else:
        return "Ismeretlen"

bolyesz = ""
while bolyesz != "vege":
    bolyesz = input("Bolygó neve: ")
    if bolyesz != "vege":
        uzi = check_planet(bolyesz)
        print(uzi) 