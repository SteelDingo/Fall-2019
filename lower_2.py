phrase = input("Type something: \n")

for letter in phrase:
    if (ord(letter) >= ord('A')) and (ord(letter) <= ord('Z')):
        lower = chr(ord('a')+ord(letter)-ord('A'))
        print(lower)
    elif (ord(letter) == ord(' ')):
        print(letter)
