year = int(input("Enter a year: \n"))

year_4 = year%4

if year_4 == 0:
    year_100 = year%100

    if year_100 != 0:
        print(f"{year} is a leap year!")

    elif year_100 == 0:
        year_400 = year%400

        if year_400 == 0:
            print(f"{year} is a leap year!")

        elif year_400 != 0:
            print(f"{year} is not a leap year.")

elif year_4 != 0:
    print(f"{year} is not a leap year.")
