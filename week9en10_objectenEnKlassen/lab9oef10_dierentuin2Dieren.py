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
        self.max = 2
        self.soort = soort
        self.dieren = []
        self.id = Kooi.id
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
            if ((newDier.soort == self.soort) or (self.soort == "all")) and (newDier.kooiId == -1) and (len(self.dieren) < self.max):
                newDier.kooiId = self.id
                self.dieren.append(newDier)

class GroteKooi(Kooi):
    def __init__(self, soort="all"):
        super().__init__(soort)
        self.max = 5

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
    

    def geef_dieren(self, *opties, type):
        if (type in ["kleur", "poten"]):
            isType = []
            for kooi in self.kooien:
                for dier in kooi.dieren:
                    if (type == "kleur"):
                        eigenschap = dier.kleur
                    elif (type == "poten"):
                        eigenschap = dier.aantalPoten
                    if (eigenschap in opties):
                        isType.append(dier.soort)
            return isType
        else:
            print(f"{type} is not a valid eigenschap, returning None")
            return None
    
    def totaal_aantal_poten(self):
        totaalPoten = 0
        for kooi in self.kooien:
            for dier in kooi.dieren:
                totaalPoten += dier.aantalPoten
        return totaalPoten

    def verhuis_dier(self, ontvangende_dierentuin, dier):
        for selfKooi in self.kooien:
            if (dier in selfKooi):
                selfKooi.dieren.remove(dier)
                for kooi in ontvangende_dierentuin.kooien:
                    if ((kooi.soort == dier.soort) or (kooi.soort == "all")) and (len(kooi.dieren) < kooi.max):
                        kooi.add_dieren(dier)
                




bart = Papegaai("groen")
jan = Schaap('zwart')
bert = Wolf()
kurt = Slang("groen")
johan = Schaap()
mark = Papegaai("oranje")
tom = Wolf("wit")
jef = Slang("blauw")
nick = Schaap("groen")
jos = Wolf("zwart")
henry = Wolf("groen")

print(tom)
print(kurt)

enkelWolven = Kooi("Wolf")
enkelWolven.add_dieren(bart, jan, bert, kurt, johan, mark, tom)
alleDierenKooi = GroteKooi()
alleDierenKooi.add_dieren(bart, jan, bert, kurt, johan, mark, tom)
kleineKooi = Kooi()
kleineKooi.add_dieren(jef, nick, jos, bart, jan, bert, kurt, johan, mark, tom)
andereKooi = Kooi()
andereKooi.add_dieren(henry, jos)

zoo = Dierentuin()
andereZoo = Dierentuin()

zoo.add_kooien(enkelWolven, alleDierenKooi)
andereZoo.add_kooien(kleineKooi, andereKooi)

print(zoo)

print(zoo.geef_dieren("groen", "oranje", "zwart", type="kleur"))

print(zoo.geef_dieren("wit", type="kleur"))

print(zoo.geef_dieren(4, type="poten"))

print(zoo.geef_dieren(2, type="poten"))

print(zoo.totaal_aantal_poten())

print(andereZoo)

print(andereZoo.geef_dieren("groen", "blauw", type="kleur"))

print(andereZoo.geef_dieren("wit", type="kleur"))

print(andereZoo.geef_dieren(4, type="poten"))

print(andereZoo.geef_dieren(2, type="poten"))

print(andereZoo.totaal_aantal_poten())