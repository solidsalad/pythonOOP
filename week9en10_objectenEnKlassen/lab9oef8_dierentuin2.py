class Dier():
    def __init__(self, aantalPoten):
        self.aantalPoten = aantalPoten
        self.kleur = "kleurloos"
        self.soort = self.__class__.__name__
        self.kooiId = -1
    
    def __str__(self):
        return(f"soort: {self.soort}\nkleur: {self.kleur}\naantal poten: {self.aantalPoten}\ngeluid: {self.geluid}\n")

class NulpotigDier(Dier):
    def __init__(self):
        super().__init__(aantalPoten=0)

class TweepotigDier(Dier):
    def __init__(self):
        super().__init__(aantalPoten=2)

class VierpotigDier(Dier):
    def __init__(self):
        super().__init__(aantalPoten=4)
        

class Wolf(VierpotigDier):
    def __init__(self, kleur="grijs"):
        super().__init__()
        self.kleur = kleur
        self.geluid = "grom"


class Schaap(VierpotigDier):
    def __init__(self, kleur="wit"):
        super().__init__()
        self.kleur = kleur
        self.geluid = "baah"


class Slang(NulpotigDier):
    def __init__(self, kleur):
        super().__init__()
        self.kleur = kleur
        self.geluid = "ssss"


class Papegaai(TweepotigDier):
    def __init__(self, kleur):
        super().__init__()
        self.kleur = kleur
        self.geluid = "baah"


class Kooi():
    id = 0
    def __init__(self, soort="all"):
        self.id = Kooi.id
        self.soort = soort
        self.dieren = []
        Kooi.id += 1
    
    def __str__(self):
        soorten = []
        for dier in self.dieren:
            soorten.append(dier.soort)
        return f'id: {self.id}\ninhoud: {", ".join(soorten)}'

    #* = splat method: je geeft een of meerdere newDieren mee gescheiden door een komma, en dezen zullen automatisch in een list gezet worden
    def add_dieren(self, *newDieren):
        for newDier in newDieren:
            #elk dier kan telkens maar in 1 kooi tegelijk zitten
            if ((newDier.soort == self.soort) or (self.soort == "all")) and (newDier.kooiId == -1):
                newDier.kooiId = self.id
                self.dieren.append(newDier)


class Dierentuin():
    def __init__(self):
        self.kooien = []

    def __str__(self):
        temp = ""
        kooiInhoud = {}
        for kooi in self.kooien:
            kooiInhoud[kooi.id] = kooi.dieren
        
        for kooi in self.kooien:
            temp += (f"kooi ID: {kooi.id}\ndieren: ")
            for dier in kooi.dieren:
                temp += (f"\n\t- {dier.soort}")
            temp += ("\n\n")
        return temp


    def add_kooien(self, *newKooien):
        for newKooi in newKooien:
            self.kooien.append(newKooi)
    

    def dieren_met_kleur(self, kleur):
        isKleur = []
        for kooi in self.kooien:
            for dier in kooi.dieren:
                if (dier.kleur == kleur):
                    isKleur.append(dier.soort)
        return isKleur


    def dieren_met_aantal_poten(self, aantalPoten):
        correctAantalPoten = []
        for kooi in self.kooien:
            for dier in kooi.dieren:
                if (dier.aantalPoten == aantalPoten):
                    correctAantalPoten.append(dier.soort)
        return correctAantalPoten
    

    def totaal_aantal_poten(self):
        totaalPoten = 0
        for kooi in self.kooien:
            for dier in kooi.dieren:
                totaalPoten += dier.aantalPoten
        return totaalPoten




bart = Papegaai("groen")
jan = Schaap('zwart')
bert = Wolf()
kurt = Slang("groen")
johan = Schaap()
mark = Papegaai("blauw")
tom = Wolf("wit")

print(tom)
print(kurt)

enkelWolven = Kooi("Wolf")
enkelWolven.add_dieren(bart, jan, bert, kurt, johan, mark, tom)
alleDierenKooi = Kooi()
alleDierenKooi.add_dieren(bart, jan, bert, kurt, johan, mark, tom)

zoo = Dierentuin()

zoo.add_kooien(enkelWolven, alleDierenKooi)

print(zoo)

print(zoo.dieren_met_kleur("groen"))

print(zoo.dieren_met_kleur("wit"))

print(zoo.dieren_met_aantal_poten(4))

print(zoo.dieren_met_aantal_poten(2))

print(zoo.totaal_aantal_poten())