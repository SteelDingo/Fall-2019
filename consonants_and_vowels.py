string = input("Type a phrase: \n")
vowels = "AaEeIiOoUu"
consonants = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"

def check_vow(string, vowels):
    final = [each for each in string if each in vowels]
    print(f"There are {len(final)} vowels.")

def check_con(string, consonants):
    final = [each for each in string if each in consonants]
    print(f"There are {len(final)} consonants.")


check_vow(string, vowels)
check_con(string, consonants)
