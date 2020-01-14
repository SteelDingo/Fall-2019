total = int(input("Enter a number between 1-86400\n\n"))
flag = 1

while flag:
    
    if total <= 0:
        print(f"Number too low.")
        #q = input("Press q to quit.\n")
        
        #if q=="q":
            #flag = 0
        #else:
            #print("Wrong letter.")

        total = int(input("Enter a number between 1-86400\n\n"))
        
    elif total <= 86400:    
        hours = total // 3600
        minutes = (total % 3600) // 60
        seconds = (total % 3600) % 60
        print(f"There are {hours} hours, {minutes} minutes, and {seconds} seconds.")
        q = input("Press q to quit.\n")
        
        if q=="q":
            flag = 0
        else:
            print("Wrong letter.")
            
    else:
        print("Number too high.")
        #q = input("Press q to quit.\n")
        
        #if q=="q":
            #flag = 0
        #else:
            #print("Wrong letter.")

        total = int(input("Enter a number between 1-86400\n\n"))

