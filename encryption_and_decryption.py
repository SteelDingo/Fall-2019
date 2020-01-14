def letters():
    letters = []
    for index in range(26):
        letters = letters + [chr(ord('a')+index)]
    return letters

def clean_phrase(phrase):
    return phrase.lower()

al = letters()

bl = al[4:] + al[:4]

encryption = dict(zip(al,bl))

choice = input("Would you like to encrypt or decrypt a message?\n")
choice_lower = str.lower(choice)

if choice_lower=="encrypt":
    phrase = input(str("Enter a string to be encrypted: \n"))
    phrase = clean_phrase(phrase)

    for letter in phrase:
        if letter in encryption:
            print(encryption[letter], end="")
        elif letter == ' ':
            print(letter, end="")

elif choice_lower=="decrypt":
    phrase = input(str("Enter a string to be decrypted: \n"))
    phrase = clean_phrase(phrase)

    decryption = dict(zip(encryption.values(),encryption.keys()))

    for letter in phrase:
        if letter in decryption:
            print(decryption[letter], end="")
        elif letter == ' ':
            print(letter, end="")
