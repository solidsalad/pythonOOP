class Dier():
    def __init__(self, aantalPoten=4):
        self.aantalPoten = aantalPoten
        self.kleur = "kleurloos"
        self.soort = self.__class__.__name__
    
    def __str__(self):
        return(f"soort: {self.soort}\nkleur: {self.kleur}\naantal poten: {self.aantalPoten}")

class Wolf(Dier):
    def __init__(self, kleur="grijs"):
        super().__init__(aantalPoten=4)
        self.kleur = kleur

class Schaap(Dier):
    def __init__(self, kleur="wit"):
        super().__init__(aantalPoten=4)
        self.kleur = kleur

class Slang(Dier):
    def __init__(self, kleur):
        super().__init__(aantalPoten=0)
        self.kleur = kleur

class Papegaai(Dier):
    def __init__(self, kleur):
        super().__init__(aantalPoten=2)
        self.kleur = kleur

class Kooi():
    def __init__(self, id, soort="all"):
        self.id = id
        self.soort = soort
        self.dieren = []
    
    def __str__(self):
        soorten = []
        for dier in self.dieren:
            soorten.append(dier.soort)
        return f'id: {self.id}\ninhoud: {", ".join(soorten)}'

    #* = splat method: je geeft een of meerdere newDieren mee gescheiden door een komma, en dezen zullen automatisch in een list gezet worden
    def add_dieren(self, *newDieren):
        for newDier in newDieren:
            if (newDier.soort == self.soort) or (self.soort == "all"):
                self.dieren.append(newDier)
        

bart = Papegaai("groen")
jan = Schaap('zwart')
bert = Wolf()
kurt = Slang("fluogeel")
johan = Schaap()
mark = Papegaai("blauw")
tom = Wolf("wit")

alleDierenKooi = Kooi(1)
alleDierenKooi.add_dieren(bart, jan, bert, kurt, johan, mark, tom)
enkelWolven = Kooi(2, "Wolf")
enkelWolven.add_dieren(bart, jan, bert, kurt, johan, mark, tom)

print(f"{alleDierenKooi}\n")
print(f"{enkelWolven}\n")



        
    

