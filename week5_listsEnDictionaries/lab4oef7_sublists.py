def isSublist(longList, shortList):
    for i in range(len(shortList)):
        if shortList[i] in longList:
            diff = longList.index(shortList[0])
            j = longList.index(shortList[i])
            if ((j - i) != diff):
                result = False
            else:
                result = True
        else:
            return False
    return result
        
print(isSublist([1,2,3,4],[2,4]))