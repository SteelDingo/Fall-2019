def clean_word(word):
    return word.strip().lower()

def wordd():
    letters = {}
    for index in range(26):
        key = chr(ord('a')+index)
        letters[key] = 0
    return letters

def letter_count(letters, word):
    for ch in word:
        if ch in letters:
            letters[ch] = letters[ch] + 1
    return letters

#input_file = open("words.txt","r")
#output_file = open("value_dictionary.txt","w")

file_str = input("Open what file: ")
flag = 0
output_file = open("dictionary.txt","w")

while not flag:
    try:
        input_file = open(file_str)
        if file_str == "words.txt":
            flag = 1
    except FileNotFoundError:
        print("The file",file_str,"doesn't exist.")
        file_str = input("Open what file: ")

while flag:
    #try:
        for line_str in input_file:
            for word in line_str:
                word = clean_word(word)
                letters = wordd[]
                letter_count = letter_count(letters, word)
            print(letter_count)

    #except TypeError:
        #if object == dict:
            #continue
