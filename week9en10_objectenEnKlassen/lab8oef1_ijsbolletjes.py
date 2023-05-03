class IjsBolletje():
    def __init__(self, smaak):
        self.smaak = smaak
    def __str__(self):
        return str(self.smaak)
    
def maak_bolletjes():
    bolletje1 = IjsBolletje("pistashe")
    bolletje2 = IjsBolletje("chocolade")
    bolletje3 = IjsBolletje("mokka")

    bolletjes = [bolletje1, bolletje2, bolletje3]

    for i in range(len(bolletjes)):
        print(f"de smaak van bolletje {i+1} is {bolletjes[i]}")


maak_bolletjes()

