def centreString(string, avSpace):
    space = int((avSpace - len(string))/2)
    if space <= 0:
        space = 0
    result = (space * " " + string + space * " ")
    return result

print(centreString("hallo", 9))

