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

file_str = input("Open what file: ")
flag = False
output_file = open("dictionary.txt","w")

while not flag:
    try:
        input_file = open(file_str)
        if file_str == "words.txt":
            flag = True
    except FileNotFoundError:
        print("The file",file_str,"doesn't exist.")
        file_str = input("Open what file: ")

letters = wordd()

for line_str in input_file:
    line_as_words = line_str.split()
    for word in line_as_words:
        word = clean_word(word)
        letters = letter_count(letters, word)
print(letters, file=output_file)

print(f"{letters}")
input_file.close()
output_file.close()
