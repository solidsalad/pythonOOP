zijden = int(input("hoeveel zijden heeft jou veelhoek (geef een getal tussen 3 en 10): "))
zijdenWoord = "a"
opties = [3,4,5,6,7,8,9,10]

if (zijden == 3):
    zijdenWoord = "drie"
elif (zijden == 4):
    zijdenWoord = "vier"
elif (zijden == 5):
    zijdenWoord = "vijf"
elif (zijden == 6):
    zijdenWoord = "zes"
elif (zijden == 7):
    zijdenWoord = "zeven"
elif (zijden == 8):
    zijdenWoord = "acht"
elif (zijden == 9):
    zijdenWoord = "negen"
elif (zijden == 10):
    zijdenWoord = "tien"
else:
    print("das ni binnen de scope eh makker")

if zijden in opties:
    print(f"dat is een {zijdenWoord}hoek")