jaar = int(input("geef mij een jaar: "))
modulus = jaar%12
dieren = ["aap","haan","hond","varken","rat","os","tijger","konijn","draak","slang","paard","geit"]

print(f"{jaar} is het jaar van de {dieren[modulus]}")
