numbers = []

answer = 1
while (answer != 0):
    answer = int(input("geef een getal: "))
    if (answer != 0):
        numbers.append(answer)

numbers.sort()

for getal in numbers:
    print(getal)