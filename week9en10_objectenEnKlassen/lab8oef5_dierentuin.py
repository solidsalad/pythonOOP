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

bart = Papegaai("groen")
jan = Schaap('zwart')
bert = Wolf()
kurt = Slang("fluogeel")

print(f"{bart}\n")
print(f"{jan}\n")
print(f"{bert}\n")
print(f"{kurt}\n")

