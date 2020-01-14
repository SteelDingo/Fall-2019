print("Function that converts yards to miles:")
#print("To run, type yards2miles(x) with your desired yards inside the parentheses.")

def yards2miles(yards):
    return yards * 0.000568182

yards = float(input("Enter yards: \n"))
miles = yards2miles(yards)

print(f"There are {miles} miles in {yards} yards.")
