def split(string):
    return list(string)

string = input(str("Type a string: \n"))

str_list = split(string)
str_list.sort()
print(', '.join(str_list))
