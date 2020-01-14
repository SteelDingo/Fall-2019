capitals = dict()

# maybe rather than 5, you want to check for key == "done" to quit the loop
count = 1
while count < 5:
    key = input(str("Name a country: \n"))
    value = input(str("Now name its capital: \n"))
    capitals[key] = value
    count += 1

#print(capitals)

# The problem asks that we print the capitals in alphabetical order.
# Those are the in the "value" of the dictionary.
# In python 3, to get a list of values we do this

capitals_list = list(capitals.values())

# now we need to sort them
capitals_alphabetical = sorted(capitals_list)

print(capitals_alphabetical)

# you can do this in one line like this
cap_a = sorted(list(capitals.values()))
print(cap_a)
