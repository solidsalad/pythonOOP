maand = input("geef mij een maand: ")

maanden31 = ["januari","maart","mei","juli","augustus","oktober","december"]
dagen = "0"
if maand in maanden31:
    dagen = "31"
elif (maand == "februari"):
    dagen = "28 of 29"
else:
    dagen = "30"

print(f"{maand} heeft {dagen} dagen")