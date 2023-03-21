import sys

AANTAL_REGELS = 10
if len(sys.argv) < 2:
    print("\nerror: no files provided")
else:
    AlleFiles = []
    for i in range(len(sys.argv) - 1):
        try:
            mijn_bestand = open(sys.argv[i+1], "r")
        except FileNotFoundError:
            print("file not found, continuing to next file")
        else:
            AlleFiles = AlleFiles + ["\n"] + mijn_bestand.readlines()
    print (''.join(AlleFiles))
