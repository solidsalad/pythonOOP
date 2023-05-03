class IjsBolletje():
    def __init__(self, smaak):
        self.smaak = smaak
    def __str__(self):
        return str(self.smaak)

class Hoorntje():
    def __init__(self, maxBolletjes):
        self.bolletjes = []
        self.maxBolletjes = maxBolletjes

    def bolletjes_toevoegen(self, *bolletjes):
        for bolletje in bolletjes:
            if (len(self.bolletjes) < self.maxBolletjes):
                self.bolletjes.append(bolletje)
    
    def __str__(self):
        smaken = []
        for bolletje in self.bolletjes:
            smaken.append(bolletje.smaak)
        return ", ".join(smaken)
    
class ReuzeHoorntje(Hoorntje):
    def __init__(self):
        super().__init__(maxBolletjes = 5)

bolletje1 = IjsBolletje("pistashe")
bolletje2 = IjsBolletje("chocolade")
bolletje3 = IjsBolletje("mokka")
bolletje4 = IjsBolletje("beans")
bolletje5 = IjsBolletje("eurocrem")
bolletje6 = IjsBolletje("framboos")

hoorntje1 = Hoorntje(3)

hoorntje1.bolletjes_toevoegen(bolletje1, bolletje2)

print(hoorntje1)

hoorntje1.bolletjes_toevoegen(bolletje3, bolletje4, bolletje5)

print(hoorntje1)

gigaNiga = ReuzeHoorntje()

gigaNiga.bolletjes_toevoegen(bolletje1, bolletje2, bolletje3, bolletje4, bolletje5, bolletje6)

print(gigaNiga)