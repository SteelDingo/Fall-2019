vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

def count_vowels(input):
    count = 0
    for ch in input:
        if ch in vowels:
            count = count + 1
    return count

def count_consonants(input):
    count = 0
    for ch in input:
        if ch in consonants:
            count = count + 1
    return count

user_string = input("Enter a string: \n")
user_lower = user_string.lower()

nvowels = count_vowels(user_lower)
nconsonants = count_consonants(user_lower)
print("The string %s has %d vowels." % (user_string, nvowels))
print("The string %s has %d consonants." % (user_string, nconsonants))
