import csv
cust_file = open("customers.csv", "a+")
order_file = open("orders.csv", "a+")
cust_reader = csv.reader(cust_file)
cust_writer = csv.writer(cust_file)

sheet_list=[]
for row in cust_reader:
    sheet_list.append(row)

def quantity(price):
    quantity=input("How many?\n")
    flag=1
    while flag:
        if quantity.isdigit():
            quant=int(quantity)
            order_price=(price*quant)
            print(order_price)          #this was just a checkpoint to see if it got this far
            flag=0
        else:
            quantity=input("Please enter a number:\n")
    return order_price, quant

#buy goods
item = input("Would you like an apple ($2), orange ($5), pear ($4), or banana ($3)?\n").upper()
flag=1
while flag:
    if item=="APPLE":
        price=2
        quantity(price)
##        print(quant)
##        print(order_price)
        flag=0
    elif item=="ORANGE":
        price=5
        quantity(price)
##        print(order_price)
        flag=0
    elif item=="PEAR":
        price=4
        quantity(price)
##        print(order_price)
        flag=0
    elif item=="BANANA":
        price=3
        quantity(price)
##        print(order_price)
        flag=0
    else:
        item = input("Would you like an apple, orange, pear, or banana?\n").upper()
        
cust_name = input("Enter your name:\n").upper()

for row in sheet_list:
    if cust_name in row:
        # item and quantity
        #cust_writer.write(item)
        continue
    else:
        # create new row
        if row[0]:
            sheet_list[0]=cust_name
##            sheet_list[1]=ID
            sheet_list[2]=item
##            sheet_list[3]=quant
            for row in sheet_list:
                cust_writer.writerow(row)
print(sheet_list)
    
cust_file.close()
