numbers = [5,7,52,89,1,6,2,6,4,8,3,6,2,5,55,5,6,2,1,5]

def delBigSmallNList(list, n):
    if (2*n < len(list)):
        list.sort()
        return list[n:(-n)]
    else:
        return "error: list too short"

print(delBigSmallNList(numbers, 9))