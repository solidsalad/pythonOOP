import random

rood = [1, 3, 5, 7, 9, 12, 14,16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
groen = [-1, 0]
randNummer = random.randint(-1,36)

#vakje
vakje = str(randNummer)
if (randNummer == -1):
    vakje = "00"

print(f"balletje is beland op vakje {vakje}\n")
print(f"Betaal {vakje}\n")


if (randNummer not in groen):
    #kleur
    if (randNummer in rood):
        kleur = "rood"
    else:
        kleur = "zwart"    
    print(f"Betaal {kleur}\n")

    #even of oneven
    if (randNummer%2 == 0):
        evenOneven = "even"
    else:
        evenOneven = "oneven"
    print(f"Betaal {evenOneven}\n")

    #welke helft
    if (randNummer > 18):
        helft = "18 t.e.m. 36"
    else:
        helft = "1 t.e.m. 18" 
    print(f"Betaal {helft}\n")

