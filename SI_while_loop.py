principle = float(input("Enter Principle amount\n"))
time = int(input("Enter time \n"))
rate = float(input("Enter rate amount\n"))


simple_interest = (principle * time * rate)/100
flag = 1

while flag:
    print(f"the simple interst is {simple_interest}")
    q = input("Press q to quit.\n")
    
    if q=="q":
        flag = 0
    else:
        print("Wrong letter.\n")
        
#else:
    #print(f"something isn't right")
