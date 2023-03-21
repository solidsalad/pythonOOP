import random
cijfers = []

while len(cijfers) < 6:
    getal = random.randint(0,49)
    if (getal not in cijfers):
        cijfers.append(getal)

print(cijfers)