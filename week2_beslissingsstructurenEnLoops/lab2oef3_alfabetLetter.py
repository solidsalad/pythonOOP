
letter = "aa"
while (len(letter) != 1):
 letter = input("geef mij een letter: ")

klinkers = ["a","e","i","o","u"]

if letter in klinkers:
    print(f"{letter} is een klinker")
elif (letter == "y"):
    print("y is soms een klinker en soms een medeklinker")
else:
    print(f"{letter} is een medeklinker")