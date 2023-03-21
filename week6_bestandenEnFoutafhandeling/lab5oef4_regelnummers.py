

filename = input("welk bestand wil je aanpassen?: ")
filenameNew = input("hoe moet het nieuwe bestand noemen?: ")

bestand = open(filename, "r")

regels = bestand.readlines()
regelNum = regels

for i in range(len(regels)):
    regelNum[i] = f"{i+1}. " + regels[i]
bestand.close()


bestandNew = open(filenameNew, "w")
bestandNew.write("".join(regelNum))
bestandNew.close()