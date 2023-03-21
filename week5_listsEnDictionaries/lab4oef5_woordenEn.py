def kommaEn(woorden):
    string1 = ", ".join(woorden[:len(woorden) - 1])
    string2 = woorden[-1]
    if (len(woorden) > 1):
        return (string1 + " en " + string2)
    else:
        return string2


test0 = ["rozen"]
test1 = ["rozen", "kranten"]
test2 = ["rozen", "kranten", "ketels"]
test3 = ["rozen", "kranten", "ketels", "wanten"]
print(kommaEn(test0))
print(kommaEn(test1))
print(kommaEn(test2))
print(kommaEn(test3))
