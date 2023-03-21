print("geef mij mensen en ik zal de totaalprijs van de inkom berekenen (geef niets in om te stoppen)")

stop = False

babyPrijs = 0.00
kidPrijs = 0.00
adultPrijs = 0.00
elderPrijs = 0.00

babyCounter = 0
kidCounter = 0
adultCounter = 0
elderCounter = 0

while (stop == False):
    persoon = input("geef een leeftijd: ")
    if (persoon == ""):
        stop = True
    else:
        leeftijd = float(persoon)

    if (leeftijd < 3):
        babyPrijs += 0
        babyCounter += 1
    elif (leeftijd < 12):
        kidPrijs += 15
        kidCounter += 1
    elif (leeftijd < 65):
        adultPrijs += 30
        adultCounter += 1
    else:
        elderPrijs += 20
        elderCounter += 1


print(f"{babyCounter} babies: €{babyPrijs}")
print(f"{kidCounter} kinderen: €{kidPrijs}")
print(f"{adultCounter} volwassenen: €{adultPrijs}")
print(f"{elderCounter} senioren: €{elderPrijs}")