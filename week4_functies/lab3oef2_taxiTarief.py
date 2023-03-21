def taxiTarief(tarief, afstand, uur, wachttijd, weekend):
    totaal = 0
    
    #tarief
    if (tarief == 'A'):
        totaal += 5
        if (weekend == True):
            totaal += 2.5
    elif (tarief == 'B'):
        totaal += 7.5
    elif (tarief == 'C'):
        totaal += 85
    print(totaal)

    #afstand
    if (tarief == 'C'):
        afstand -= 50
    
    if (afstand > 0):
        totaal += afstand * 2.5
    print(totaal)

    #uur
    if (uur >= 22) or (uur <= 6):
        totaal += 2.5
    print(totaal)

    #wachttijd
    wachttijd = round((wachttijd-0.5), None)
    if (wachttijd >= 0):
        totaal += wachttijd * 45
    
    return totaal

print(taxiTarief('C', 55, 23, 0, True))
    
    