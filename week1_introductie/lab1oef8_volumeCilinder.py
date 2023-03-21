import math

straal = float(input("geeft mij een straal (in meter): "))
hoogte = float(input("geeft mij een hoogte (in meter): "))

volume = (math.pi)*(pow(straal, 2)*hoogte)

print(f"een cilinder met een grondvlak met straal {straal}m en een hoogte {hoogte}m heeft een volume van {round(volume,2)}m³")