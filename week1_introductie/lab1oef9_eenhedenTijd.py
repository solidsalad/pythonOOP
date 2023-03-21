dagen = int(input("uit hoeveel dagen bestaat je tijdseenheid? "))
uren = int(input(f"{dagen} dagen, en hoeveel uren? "))
minuten = int(input(f"{dagen} dagen, {uren} uren, en hoeveel minuten? "))
seconden = int(input(f"{dagen} dagen, {uren} uren, {minuten} minuten, en hoeveel seconden? "))

totaalSeconden = seconden + (minuten*60) + (uren*60*60) + (dagen*60*60*24)

print(f"{dagen} dagen, {uren} uren, {minuten} minuten, en {seconden} seconden is gelijk aan: {totaalSeconden} seconden.")
