flesKlein = 0.12
flesGroot = 0.25

hvlGroot = float(input("hoeveel grote flessen lever je in? "))
hvlKlein = float(input("hoeveel kleine flessen lever je in? "))

teruggave = round(((hvlGroot*flesGroot)+(hvlKlein*flesKlein)), 2)

print(f"je krijgt €{teruggave} terug")