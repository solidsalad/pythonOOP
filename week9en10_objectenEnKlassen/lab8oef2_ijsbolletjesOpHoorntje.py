class IjsBolletje():
    def __init__(self, smaak):
        self.smaak = smaak
    def __str__(self):
        return str(self.smaak)

class Hoorntje():
    def __init__(self):
        self.bolletjes = []
    
    def bolletjes_toevoegen(self, *bolletjes):
        for bolletje in bolletjes:
            self.bolletjes.append(bolletje)
    
    def __str__(self):
        smaken = []
        for bolletje in self.bolletjes:
            smaken.append(bolletje.smaak)
        return ", ".join(smaken)
    
bolletje1 = IjsBolletje("pistashe")
bolletje2 = IjsBolletje("chocolade")
bolletje3 = IjsBolletje("mokka")

hoorntje1 = Hoorntje()

hoorntje1.bolletjes_toevoegen(bolletje1, bolletje2, bolletje3)

print(hoorntje1)