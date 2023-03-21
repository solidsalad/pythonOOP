text = []

answer = "1"
while (answer != ""):
    answer = input("geef woord: ")
    if (answer != "") and (answer not in text):
        text.append(answer)

for word in text:
    print(word)
        

