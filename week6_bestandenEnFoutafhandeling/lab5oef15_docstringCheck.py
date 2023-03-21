import sys
if len(sys.argv) < 2:
    print("\nerror: no files provided")
    
    #een voor een door alle parameters loopen
    for i in range(len(sys.argv) - 1):
        docstringIncluded = False
        functionPresent = False
        
        #checken of bestand bestaat, zo ja -> omzetten naar list
        try:
            mijn_bestand = open(sys.argv[i+1], "r")
        except FileNotFoundError:
            print(f"\nfile [{sys.argv[i+1]}] not found, continuing to next file")
        else:
            file = sys.argv[i+1]
            j = 0
            array = mijn_bestand.readlines()
            
            #checking if a function gets declared the script, and next line contains ''' (docstring)
            for line in array:
                #arrayindex van "line" op een leesbare manier bijhouden
                j += 1
                if ("def" in line):
                    functionPresent = True
                    if ("'''" in array[j]) or ("\"\"\"" in array[j]):
                        docstringIncluded = True
            
            #resultaten printen
            if functionPresent == True and docstringIncluded == True:
                print(f"\ngoed zo, je includeerde een docstring in {file}")
            elif functionPresent == True and docstringIncluded == False:
                print(f"\ngodverdomme schijtedebiel, ge hebt geen docstring in [{file}] toegevoegd")
            else:
                print(f"\n[{file}] bevat geen functies, en hoeft dus ook geen docstring te hebben")
            
