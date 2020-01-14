import math
principal_str = input("Enter the principal amount: ")
principal_float = float(principal_str)

duration_str = input("Enter the time period: ")
duration_float = float(duration_str)

rate_str = input("Enter the interest rate: ")
rate_float = float(rate_str)
rate_pkmn = rate_float / 100

SI = (principal_float * duration_float * rate_pkmn)
print("The simple interest is:", SI)
