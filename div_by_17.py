print("Triple-digit numbers divisible by 17:")
c = 100

while c <= 999:
    c_mod = c % 17
    
    if c_mod == 0:
        print(f"{c}")
        
    c += 1

    #elif c_mod != 0:
        
