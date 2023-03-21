
def capitalizeText(string):
    wordArr = string.split(" ")
    for i in range(len(wordArr)):
        if i > 0:
            if ('?' in wordArr[i-1]) or ('!' in wordArr[i-1]) or ('.' in wordArr[i-1]):
                wordArr[i] = wordArr[i].capitalize()
        else:
            wordArr[i] = wordArr[i].capitalize()
    print(' '.join(wordArr))


zin = input("geef mij een tekst: ")
capitalizeText(zin)

