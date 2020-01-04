import csv
periodic_file = open("Periodic-Table.csv", "r",encoding="windows-1252")
#reader = csv.reader(periodic_file)

line_count = 1
for line in periodic_file:
    #if line > 4:
    cells = line.split(',')
    line_count = line_count + 1

symbol = symbol_dict={}
group = group_dict={}
period = period_dict={}

symbol[cells[0]] = cells[1]
group[cells[0]] = cells[2]
period[cells[0]] = cells[4]

print(symbol)
print(group)
print(period)
