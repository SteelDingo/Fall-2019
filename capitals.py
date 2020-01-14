capitals = dict()

count = 1
while count < 5:
    key = input(str("Name a country: \n"))
    value = input(str("Now name its capital: \n"))
    capitals[key] = value
    count += 1

cap_a = sorted(list(capitals.values()))
print(cap_a)
