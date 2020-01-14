import math
S = input("Enter a number 1-86400: ")

S_int  = int(S) # change S to int since the prompt is str
hours = int(S_int/3600)
S_hoursRemoved = S_int % 3600

minutes = int(S_hoursRemoved/60)

seconds = S_hoursRemoved % 60

print("The time is:", hours,":", minutes,":", seconds)
