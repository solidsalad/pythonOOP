print("geef mij waarden en ik zal het gemiddelde berekenen (geef 0 in om te stoppen)")

stop = False
totaal = 0
counter = 0

while (stop == False):
    getal = float(input("geef een getal: "))
    totaal += getal

    if (getal == 0):
        stop = True
    else:
        counter += 1

gemiddelde = (totaal/counter)

print(f"het gemiddelde is: {gemiddelde}")
