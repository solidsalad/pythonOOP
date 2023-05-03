class Drank():
    def __init__(self, name, idealTemp=20):
        self.name = name
        self.idealTemp = idealTemp
    
    def log_drank(self, file):
        file.log_string(f"drink name: {self.name}\nideal temperature: {self.idealTemp}°C\n\n")
    

class LogFile():
    def __init__(self, bestandsnaam, writeMode="w"):
        self.bestandsnaam = bestandsnaam
        self.bestand = open(bestandsnaam, mode=writeMode, encoding="utf-8")
    
    def log_string(self, string):
        self.bestand.write(string)


liquidNitrogen = Drank("liquid nitrogen", -195.8)
depletedPlutonium = Drank("depleted plutonium", 639.4)
eurocrem = Drank("eurocrem")
moltenTungsten = Drank("molten fucking tungsten", 3422)

print(eurocrem.idealTemp)

logFile = LogFile("yummy.txt")

moltenTungsten.log_drank(logFile)
depletedPlutonium.log_drank(logFile)