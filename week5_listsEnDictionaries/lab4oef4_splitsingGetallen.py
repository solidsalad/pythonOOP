negatives = []
zeros = []
positives = []

answer = 1
while (answer != ""):
    answer = input("geef een getal: ")
    if (answer != ""):
        answer = int(answer)
        if (answer < 0):
            negatives.append(answer)
        elif (answer == 0):
            zeros.append(answer)
        elif (answer > 0):
            positives.append(answer)
    
listAll = negatives + zeros + positives

for number in listAll:
    print(number)