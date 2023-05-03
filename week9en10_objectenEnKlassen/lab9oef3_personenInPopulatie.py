class Persoon():
    populatie = 0
    
    def __init__(self, naam):
        self.naam = naam
        Persoon.populatie += 1

    def __del__(self):
        Persoon.populatie -= 1



jan = Persoon("jan")
gert = Persoon("gert")
michiel = Persoon("michiel")
kurt = Persoon("kurt")
gucci = Persoon("gucci")

print(Persoon.populatie)

del gucci

print(Persoon.populatie)