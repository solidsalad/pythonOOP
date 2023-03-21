for i in range(100):
    fizzbuzz = ""
    if (i%3 == i%5 == 0):
        fizzbuzz = "Fizzbuzz"
    elif (i%3 == 0):
        fizzbuzz = "Fizz"
    elif (i%5 == 0):
        fizzbuzz = "Buzz"

    if (fizzbuzz != ""):
        print(fizzbuzz)
    else:
        print(i)