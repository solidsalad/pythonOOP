def verzendkosten(aantalArtikels):
    totaal = 5.5 + (aantalArtikels * 3)
    if aantalArtikels <= 0:
        totaal = 0
    return totaal

def verzending():
    artikels = int(input("hoeveel artikels heb je gekocht? "))
    kosten = verzendkosten(artikels)
    print(f"aantal gekochte artikels: {artikels}\nverzendkosten: €{kosten}")

verzending()
    