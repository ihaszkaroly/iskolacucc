
class Grower:
    def read_file(self):
        fp = open('ac.txt', 'r')
        lines = fp.readlines()
        fp.close()

        self.products = []

        for line in lines[1::]:
            (id, name, price, quantity) = line.split(';')
            product = Product(id, name, price, quantity)
            self.products.append(product)
    
    # legdrágább zöldség
    def larger(self):
        pass
    
    # Az összes paprika ára
    def calcPepperPrice(self):
        pass

    # Mennyi a vöröshagyma és a karalábé tömege együtt?
    def sumOnionKohlrabiWeight(self):
        pass
    
    # Mi a neve legnagyobb tömegű zöldségnek?
    def showLargerWeight(self):
        pass
    
    # Van karalábé?
    def isHaveKohlrabi(self):
        pass

    # Hány zöldség drágább mint 700 Ft.
    def moreThenSevenhundred(self):
        pass
        

