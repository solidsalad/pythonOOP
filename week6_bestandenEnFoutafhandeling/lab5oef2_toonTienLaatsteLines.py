import sys

AANTAL_REGELS = 10

try:
    mijn_bestand = open(sys.argv[1], "r")
except IndexError:
    print("no file provided")
except FileNotFoundError:
    print("file not found")
else:
    eerstetienLines = mijn_bestand.readlines()[-AANTAL_REGELS:]
    for line in eerstetienLines:
        print(line)