import csv
from itertools import islice
periodic_file = open("Periodic-Table.csv", "r",encoding="windows-1252")
#file = csv.reader(periodic_file)
#next(periodic_file, None)
file = islice(periodic_file, 8, None)

symbol = symbol_dict={}
group = group_dict={}
period = period_dict={}

line_count = 1
for line in file:
    #if line in range(7):
        #pass
    #line = int(line)

    #for:
    cells = line.split(',')
    #print(len(cells))
    for cells in file:
        if len(cells) < 1:
            pass
        
        symbol[cells[0]] = cells[1]
        group[cells[0]] = cells[2]
        period[cells[0]] = cells[4]

    line_count = line_count + 1
    if line_count == 118:
        print("test")
        break

print(symbol)
print(group)
print(period)
