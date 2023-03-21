woord = input("geef mij een woord en ik zal checken of het een palindroom is: ")

def IsPalindroom(woord):
    result = True
    woord = woord.lower()
    for i in range(len(woord)):
        if (woord[i] != woord[len(woord)-1 - i]):
            result = False   
    return result

if (IsPalindroom(woord) == True):
    print(f"{woord} is een palindroom")
else:
    print(f"{woord} is geen palindroom")