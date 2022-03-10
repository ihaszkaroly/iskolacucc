

class Brig:
    def read_file(self):
        fp = open('datas.txt', 'r')
        lines = fp.readlines()
        fp.close()

        self.bridges = []

        for line in lines[1::]:
            (id, name, place, length, year) = line.split(':')
            bridge = BridgeModel(id, name, place, int(length), int(year))
            self.bridges.append(bridge)

    # Leghosszabb híd
    def longest(self):
        pass

    # A Megyeri híd szerepel a listában?
    def isHaveMegyeri(self):
        pass
    
    # A nem budapesti hidak nobp.txt fájlba
    def select_nobp(self):
        for bridge in self.bridges:
            if bridge.place != 'Miskolc':
                self.write_bridge(bridge)
        

    # Híd kiírása
    def write_bridge(self, bridge):
        fp = open('potlas.txt', 'w')
        fp.write(bridge.id)
        fp.write(':')
        fp.write(bridge.name)
        fp.write(':')
        fp.write(bridge.place)
        fp.write('\n')
        fp.close()


 
