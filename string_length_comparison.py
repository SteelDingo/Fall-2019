str_1 = input("String 1: \n")
str_2 = input("String 2: \n")

str_1_len = len(str_1)
str_2_len = len(str_2)

if str_1_len < str_2_len:
    print(str_1)
elif str_1_len > str_2_len:
    print(str_2)
else:
    print("The strings are the same length.")
