renteJaar = 0.012
bedrag = float(input("wat is je startbedrag op je bankrekening? "))
jaren = 80
for i in range(jaren):
    i = i+1
    bedrag = (bedrag + bedrag*renteJaar)
    print(f"na {i} jaar zal je bedrag €{round(bedrag, 2)} zijn")