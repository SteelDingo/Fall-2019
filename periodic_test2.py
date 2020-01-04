import csv
def read_table(a_file, a_dict):
    data_reader = csv.reader(a_file)

    for row in data_reader:
        if row[0].isdigit():
            symbol_str = row[1]
            a_dict[symbol_str] = row[:8]

def parse_element(element_str):
    symbol_str = ""
    quantity_str = ""
    for ch in element_str:
        if ch.isalpha():
            symbol_str = symbol_str + ch
        else:
            quantity_str = quantity_str + ch
    if quantity_str == "":
        quantity_str = "1"
    return symbol_str, int(quantity_str)


periodic_file = open("Periodic-Table.csv", "r",encoding="windows-1252")

periodic_dict={}
read_table(periodic_file, periodic_dict)

compound_str = input("Input a chemical compound, hyphenated, e.g. C-02: ")
compound_list = compound_str.split("-")

mass_float = 0.0
print("The compound is composed of: ", end=" ")

for c in compound_list:
    symbol_str, quantity_int = parse_element(c)
    print(periodic_dict[symbol_str][5], end=" ")
    mass_float = mass_float + quantity_int *\
                 float(periodic_dict[symbol_str][6])

print("\n\nThe atomic mass of the compound is", mass_float)

periodic_file.close()
