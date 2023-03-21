def magischeDatum(datum):
    datumArr = datum.split('/')
    dag = int(datumArr[0])
    maand = int(datumArr[1])
    jaar = datumArr[2]
    if ((dag * maand) == int(jaar[2] + jaar[3])):
        result = True
    else:
        result = False
    return result

def printdatum(dag, maand, jaar):
    print(f"{dag+1}/{maand+1}/{jaar+1}")

for jaar in range(1900,2000):
    for maand in range(12):
        if maand+1 in [1,3,5,7,8,10,12]:
            for dag in range(31):
                if magischeDatum(f"{dag+1}/{maand+1}/{jaar+1}") == True:
                    printdatum(dag, maand, jaar)
        elif maand+1 in [4,6,9,11]:
            for dag in range(30):
                if magischeDatum(f"{dag+1}/{maand+1}/{jaar+1}") == True:
                    printdatum(dag, maand, jaar)
        else:
            if (jaar%400 == 0) or ((jaar%4 == 0) and (jaar%100 != 0)):
                for dag in range(29):
                    if magischeDatum(f"{dag+1}/{maand+1}/{jaar+1}") == True:
                        printdatum(dag, maand, jaar)
            else:
                for dag in range(28):
                    if magischeDatum(f"{dag+1}/{maand+1}/{jaar+1}") == True:
                        printdatum(dag, maand, jaar)

            

    