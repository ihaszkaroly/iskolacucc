from operator import le
from starModel import StarModel
from typing import List
class Star:
    def __init__(self):
        self.file_name = 'stars.txt'
        self.lines = []
        self.stars: List[StarModel] = []
    
    def read_content(self):
        fp = open(self.file_name, 'r', encoding="utf-8")
        self.lines = fp.readlines()
        fp.close()
    
    def convert_content(self):
        for line in self.lines[1::]:
            (name, constellation, 
            distance, mass, temperature, age) = line.split(':')
            
            starModel = StarModel(
                name, constellation, 
                float(distance.replace(",",".")), 
                float(mass.replace(',', '.')), 
                int(temperature), 
                float(age.replace(',', '.')))

            self.stars.append(starModel)
    
    def print_out(self):
        for star in self.stars:
            print(star.name)
            print(star.constellation)
    
    # Van-e csillag a Göncöl csillagképben
    def star_in_goncol(self):
        i = 0
        n = len(self.stars)
        while i < n and self.stars[i].constellation.find("Göncöl") == -1:
            i +=1 
        if i<n:
            print("Van")
        else:
            print("Nincs")

    # Legtávolabbi csillag neve, távolsága
    def farthest_star(self):
        max_star = self.stars[0]
        for star in self.stars:
            if star.distance > max_star.distance:
                max_star = star
        print("Legtávolabbi:",max_star.name,max_star.distance)

    # Legalacsonyabb hőmérsékletű csillag
    def lowest_temperature_star(self):
        min_star = self.stars
        for star in self.stars:
            if star.temperature < min_star.temperature:
                min_star = star
        print("Legalacsonyabb hőmérséklet:",min_star.temperature)

    # A Csillagok átlagéletkor
    def average_age_of_stars(self):
        osszeg = 0
        for star in self.stars:
            osszeg += star.age
        darab = len(self.stars)
        atlag = osszeg/darab
        print("Átlag: %.2f"%atlag)

    # a Kepler-18 hány kiloggram tömegű
    def weight_of_kepler18(self):
        for star in self.stars:
            if star.name == "Kepler-18":
                print("A csillag tömege:",star.mass)
            
    # 150 fényévnél közelbbi bolygók neve és távolsága
    def close_stars(self):
        for star in self.stars:
            if star.distance < 150:
                print(star.name,star.distance)

    # A Szextánok csillagképben található csillagok adatai
    def szextan_datas(self):
        for star in self.stars:
            if star.constellation == "Szextánok":
                print(
                    star.name,
                    star.constellation,
                    star.distance,
                    star.mass,
                    star.temperature,
                    star.age
                )

    # A 2 M-nél kisebb tömegű csillagok neve és tömege
    def less_than_two_mass_stars(self):
        for star in self.stars:
            if star.mass < 2:
                print(star.name,star.mass)


star = Star()
star.read_content()
star.convert_content()
star.star_in_goncol()
star.farthest_star()
star.lowest_temperature_star()
star.average_age_of_stars()
star.weight_of_kepler18()
star.close_stars()
star.szextan_datas()
star.less_than_two_mass_stars()