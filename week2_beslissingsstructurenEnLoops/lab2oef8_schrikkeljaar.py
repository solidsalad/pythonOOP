jaar = int(input("geef mij een jaar: "))

if (jaar%400 == 0) or ((jaar%4 == 0) and (jaar%100 != 0)):
    print(f"{jaar} is een schrikkeljaar")
else:
    print(f"{jaar} is geen schrikkeljaar")
