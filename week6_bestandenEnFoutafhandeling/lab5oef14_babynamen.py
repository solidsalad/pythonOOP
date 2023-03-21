#for jaar in range(1900, 2013):
#    boys = open(f"labo5-datasets/baby_namen/{jaar}_BoysNames.txt", "r")
#    boyNames = []
#    bYearNames = boys.readlines()
#    for i in range(len(bYearNames)):
#        name = bYearNames[i].split(" ")[0]
#        if name not in boyNames:
#            boyNames.append(name)
#    boys.close()
#
#    girls = open(f"labo5-datasets/baby_namen/{jaar}_GirlsNames.txt", "r")
#    girlNames = []
#    gYearNames = girls.readlines()
#    for i in range(len(gYearNames)):
#        name = gYearNames[i].split(" ")[0]
#        if name not in girlNames:
#            girlNames.append(name)
#    girls.close()
#
#boyNames.sort()
#allBoys = open("boys.txt", "w")
#allBoys.write("\n".join(boyNames))
#allBoys.close()
#
#girlNames.sort()
#allGirls = open("girls.txt", "w")
#allGirls.write("\n".join(girlNames))
#allGirls.close()

for jaar in range(1900, 2013):
    boys = open(f"labo5-datasets/baby_namen/{jaar}_BoysNames.txt", "r")
    boyNames = {}
    bYearNames = boys.readlines()
    for i in range(len(bYearNames)):
        name = bYearNames[i].split(" ")[0]
        amount = int(bYearNames[i].split(" ")[1])
        if name not in boyNames:
            boyNames[name] = amount
        else:
            boyNames[name] = boyNames[name] + amount
    boys.close()

    girls = open(f"labo5-datasets/baby_namen/{jaar}_BoysNames.txt", "r")
    girlNames = {}
    gYearNames = girls.readlines()
    for i in range(len(gYearNames)):
        name = gYearNames[i].split(" ")[0]
        amount = int(gYearNames[i].split(" ")[1])
        if name not in girlNames:
            girlNames[name] = amount
        else:
            girlNames[name] = girlNames[name] + amount
    boys.close()

allBoys = open("boys.txt", "w")
for key in boyNames:
    allBoys.write(f"{key} : {boyNames[key]}\n")
allBoys.close()

allGirls = open("boys.txt", "w")
for key in girlNames:
    allGirls.write(f"{key} : {girlNames[key]}\n")
allGirls.close()
