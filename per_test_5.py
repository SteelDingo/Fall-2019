import csv

def dictionaries(periodic_file):
    data_reader = csv.reader(periodic_file)
    for line in data_reader:
        if line[0].isdigit():
            symbol_str = line[1]
            symbol_dict[symbol_str] = line[:8]

            number_str = line[0]
            number_dict[number_str] = line[:8]
    
            if line[2] in group_dict:
                group_dict[line[2]].append(line[:8])
            else:
                group_dict[line[2]] = [line[:8]]

            if line[4] in period_dict:
                period_dict[line[4]].append(line[:8])
            else:
                period_dict[line[4]] = [line[:8]]
    return symbol_dict, group_dict, period_dict, number_dict
    
def symbol_sort(symbol_dict):
    print("Sorting periodic table by symbol.")
    print("Sorting periodic table by symbol.\n", file=display_file)
    symbol_sorted = sorted(symbol_dict.items())
    print(symbol_sorted)
    print(symbol_sorted, file=display_file)

def number_sort(number_dict):
    print("Sorting periodic table by number.")
    print("Sorting periodic table by number.\n", file=display_file)
    int_number_dict = {int(k):v for k,v in number_dict.items()}
    number_sorted = sorted(int_number_dict.items())
    print(number_sorted)
    print(number_sorted, file=display_file)


periodic_file = open("Periodic-Table.csv", "r", encoding="windows-1252")
display_file = open("Screen-Display.txt","w")
symbol_dict={}
group_dict={}
period_dict={}
number_dict={}

alkali_metals=[3,11,19,37,55,87]
alkaline_earth_metals=[4,12,20,38,56,88]
lanthanoids=[57,58,59,60,61,62,63,64,65,66,67,68,69,70,71]
actinoids=[89,90,91,92,93,94,95,96,97,98,99,100,101,102,103]
transition_metals=[21,22,23,24,25,26,27,28,29,30,39,40,41,42,43,44,45,46,47,48,72,73,74,75,76,77,78,79,80,104,105,106,107,108,112]
post_transition_metals=[13,31,49,50,81,82,83,84,114]

metals = {'alkali metals': alkali_metals, 'alkaline earth metals': alkaline_earth_metals, 'lanthanoids': lanthanoids, 'actinoids': actinoids, 'transition metals': transition_metals, 'post transition metals': post_transition_metals}

dictionaries(periodic_file)

check = 1
marker = 1
while check:
    while marker==1:
        initial_yn = str.lower(input("Welcome. Would you like to view a specific element? Y/N "))
        print("Session log:\n", file=display_file)
        if initial_yn == "y":
            user_input = input("Enter the atomic number: ")
            #user_int = int(user_input)
            flag = 1
            while flag:
                if user_input.isdigit():
                    user_int = int(user_input)
                    #user_input = input("Please enter the atomic number: ")
                    if user_int > 118:
                        user_input = input("Number too high. Enter an atomic number: ")
                        user_int = int(user_input)
                    elif user_int < 1:
                        user_input = input("Number too low. Enter an atomic number: ")
                        user_int = int(user_input)
                    elif user_int == 117:
                        user_input = input("No data. Enter a different atomic number: ")
                        user_int = int(user_input)
                    else:
                        flag = 0
                else:
                    user_input = input("Please enter an atomic number: ")
            details = number_dict[user_input]
            print(f"Element: {details[5]}\nAtomic Symbol: {details[1]}\nAtomic Number: {details[0]}\nAtomic Mass: {details[6]}\nGroup: {details[2]}\nPeriod: {details[4]}")
            print(f"Element: {details[5]}\nAtomic Symbol: {details[1]}\nAtomic Number: {details[0]}\nAtomic Mass: {details[6]}\nGroup: {details[2]}\nPeriod: {details[4]}", file=display_file)
            for k, v in metals.items():
                if user_int in v:
                    itr = 1
                    if itr:
                        print(f"{details[1]} is in the {k} metal group.")
                        print(f"{details[1]} is in the {k} metal group.\n", file=display_file)
                    else:
                        print(f"{details[1]} is not a metal.")
                        print(f"{details[1]} is not a metal.", file=display_file)
            marker = 2
        elif initial_yn == "n":
            marker = 2
        else:
            print("Please select Y/N.")
    while marker==2:
        symbol_yn = str.lower(input("Would you like to sort by atomic symbol? Y/N "))
        if symbol_yn == "y":
            symbol_sort(symbol_dict)
            marker = 3
        elif symbol_yn == "n":
            marker = 3
        else:
            print("Please select Y/N.")
    while marker==3:
        number_yn = str.lower(input("Would you like to sort by atomic number? Y/N "))
        if number_yn == "y":
            number_sort(number_dict)
            marker = 4
        elif number_yn == "n":
            marker = 4
        else:
            print("Please select Y/N.")
    while marker==4:
        group_yn = str.lower(input("Would you like to view a group of elements? Y/N "))
        if group_yn == "y":
            group_view = input("Select a group of elements to view: ")
            flag = 1
            while flag:
                if group_view.isdigit():
                    group_int=int(group_view)
                    if group_int > 18:
                        group_view = input("Number too high. Select a group: ")
                    elif group_int < 1:
                        group_view = input("Number too low. Select a group: ")
                    else:
                        group_select = group_dict[str(group_view)]
                        flag = 0
                elif group_view == "lanthanides":
                    group_select = group_dict[str(group_view)]
                    flag = 0
                elif group_view == "actinides":
                    group_select = group_dict[str(group_view)]
                    flag = 0
                else:
                    group_view = input("Please enter a group: ")       
            print(f"Group {group_view} elements: {group_select}")
            print(f"Group {group_view} elements: {group_select}\n", file=display_file)
            marker = 5
        elif group_yn == "n":
            marker = 5
        else:
            print("Please select Y/N.") 
    while marker==5:
        period_yn = str.lower(input("Would you like to view a period of elements? Y/N "))
        if period_yn == "y":
            period_view = input("Select a period of elements to view: ")
            flag = 1
            while flag:
                if period_view.isdigit():
                    period_int=int(period_view)
                    if period_int > 7:
                        period_view = input("Number too high. Select a period: ")
                    elif period_int < 1:
                        period_view = input("Number too low. Select a period: ")
                    else:
                        period_select = period_dict[str(period_view)]
                        flag = 0
                else:
                    period_view = input("Please enter a period: ")
            print(f"Period {period_view} elements: {period_select}")
            print(f"Period {period_view} elements: {period_select}\n", file=display_file)
            marker = 6
        elif period_yn == "n":
            marker = 6
        else:
            print("Please select Y/N.")
    while marker==6:
        again_yn = str.lower(input("Do you want to view another element? Y/N "))
        if again_yn == "y":
            marker = 1
        elif again_yn == "n":
            check = 0
            marker = 0
        else:
            print("Please select Y/N.")
            marker = 6
while not check:
    print('All relevant information has been recorded to file "Screen-Display."')
    break

periodic_file.close()
display_file.close()
