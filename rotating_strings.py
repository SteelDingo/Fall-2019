print("Roatating characters in a string over one and the last character to the front.")
str_1 = input("Type something: \n")

def rotate_string(input):
    return str_1[-1] + str_1[:-1]


#str_2 = str_1[-1] + str_1[:-1]

print(rotate_string(input))
