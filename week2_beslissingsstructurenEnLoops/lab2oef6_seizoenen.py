maand = input("geef mij een maand: ")
dag = int(input("geef mij een dag: "))

winter = ["januari", "februari"]
lente = ["maart", "april", "mei"]
zomer = ["juni", "juli", "augustus"]

if (maand in winter) or (maand == "december" and dag > 20) or (maand == "maart" and dag < 21):
    print("winter")
elif (maand in lente) or (maand == "juni" and dag < 21):
    print("lente")
elif (maand in zomer) or (maand == "september" and dag < 21):
    print("zomer")
else:
    print("herfst")