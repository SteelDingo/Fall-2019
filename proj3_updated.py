import csv
import random

customer_file = 'customers.csv'
order_file = 'orders.csv'

def load_customer_ids():
    customers = []
    with open(customer_file) as fh:
        reader = csv.reader(fh, delimiter=',')
        for row in reader:
            customer = {'Customer Name': row[0], 'Customer ID': row[1]}
            customers.append(customer)
    return customers

def add_customer_id(cust_name, cust_id):
    with open(customer_file, mode='a', newline='') as fh:
        writer = csv.writer(fh, delimiter=',')
        writer.writerow([cust_name, cust_id])

def add_customer_order(cust_id, item, quantity, price_per):
    price_total = price_per * quantity
    with open(order_file, mode='a', newline='') as fh:
        writer = csv.writer(fh, delimiter=',')
        writer.writerow([cust_id, item, quantity, price_per, price_total])

def get_customer_id(customers, name):
    cust_id = None
    for customer in customers:
        if customer['Customer Name'] == name:
            cust_id = customer['Customer ID']
    return cust_id

def is_id_used(customers, cust_id):
    used = False
    for customer in customers:
        if customer['Customer ID'] == cust_id:
            used = True
    return used

def new_customer_id(customers):
    used = True
    while used:
        cust_id = random.randint(10000, 99999)
        used = is_id_used(customers, cust_id)
    return cust_id

price_list = {'SWORD':10, 'SHIELD':8, 'ARMOR':15, 'POTION':5}

def buy_goods(customers):
    cust_name=str.upper(input("Welcome to the store, can I get your name?\n"))
    cust_id=get_customer_id(customers, cust_name)
    if cust_id is None:
        cust_id = new_customer_id(customers)
        add_customer_id(cust_name, cust_id)

    print("Inventory:\nSword: $10\nShield: $8\nArmor: $15\nPotion: $5")
    item = str.upper(input("What item are you going to buy?\n"))
    quantity = int(input("How many would you like?\n"))
    add_customer_order(cust_id, item, quantity, price_list[item])
    print(f"Thank you for the order {cust_name}. Your ID is {cust_id}")
    print(f"You just purchased {quantity} of the item {item}")

def ID_search():
    cust_id = input("Enter the customer ID to search for that customer's orders:\n")
    with open(order_file) as fh:
        reader = csv.reader(fh, delimiter=',')
        flag=1
        for row in reader:
            if cust_id in row:
                print(row)
                flag=0
        if flag:
            print("Sorry, it appears you're not in the system.")
    return

def sales():
    print("Total sales between all customers:")
    with open(order_file) as fh:
        reader = csv.reader(fh, delimiter=',')
        total_sales = sum(int(row[4]) for row in reader)
        print("$",total_sales)
    return

def quantity_sold(quant_sold):
    with open(order_file) as fh:
        reader = csv.reader(fh, delimiter=',')
        for row in reader:
            if row[1] in quant_sold:
                quant_sold[row[1]] += int(row[2])
    return quant_sold

def item_totals(item_sales):
    with open(order_file) as fh:
        reader = csv.reader(fh, delimiter=',')
        for row in reader:
            if row[1] in item_sales:
                item_sales[row[1]] += int(row[4])
    return item_sales

customers = load_customer_ids()
#print(customers)
buy_goods(customers)
#NOTE: you must re-load customers after you buy_goods since that function will update the CSV file
customers = load_customer_ids()
print(customers)

ID_search()

sales()

quant_sold = {'SWORD': 0, 'SHIELD': 0, 'ARMOR': 0, 'POTION': 0}
item_sales = {'SWORD': 0, 'SHIELD': 0, 'ARMOR': 0, 'POTION': 0}
quantity_sold(quant_sold)
item_totals(item_sales)
print("Total quantities sold by item:")
print(quant_sold)
print("Earnings per item:")
print(item_sales)
