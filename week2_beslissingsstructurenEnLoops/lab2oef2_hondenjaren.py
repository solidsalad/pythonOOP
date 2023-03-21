mensJaren = float(input("geef de leeftijd van je hond in jaren: "))
hondJaren = 0.0

if (mensJaren >= 2):
    hondJaren = (2*10.5) + ((mensJaren-2)*4)
    print(f"je hond is {hondJaren} jaar in hondenjaren")
elif (mensJaren > 0):
    hondJaren = mensJaren*10.5
    print(f"je hond is {hondJaren} jaar in hondenjaren")
else:
    input("ah ja man efkes een hond me een negatieve leeftijd, zo koop ik mijn honden ook altijd man.")

