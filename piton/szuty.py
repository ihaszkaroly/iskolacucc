class kerekpar:
    sebesseg = 0

    def __init__(self, szin):
        self.sebesseg = 0
        self.szin = szin

    def novelseb(self):
        self.sebesseg = self.sebesseg + 1
    def telikido(self):
        while True:
            self.novelseb()
            cmd = input(">")
            if cmd == "vege":
                exit()
kerekpar.telikido()