import math as m
def Pythagoras(zijde1, zijde2):
    zijde3 = m.sqrt(m.pow(zijde1, 2) + m.pow(zijde2, 2))
    return zijde3

def VraagDriehoek():
    zijde1 = float(input("geef mij de lengte van zijde 1: "))
    zijde2 = float(input("geef mij de lengte van zijde 2: "))
    zijde3 = Pythagoras(zijde1, zijde2)
    print(zijde3)

VraagDriehoek()