def zoekMediaan(getal1, getal2, getal3):
    array = [getal1, getal2, getal3]
    array.sort()
    result = array[1]
    return result

print(zoekMediaan(4,3,8))