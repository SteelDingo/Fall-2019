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

# first we must create the dictionary before we enter the loop
# we create it only once. If we call wordd within the loop, we'd keep
# creating new dictionaries (and lose the old dictionary)
letters = wordd()

# we don't want to loop here since we're only doing this once (over the whole file)
#while flag:
for line_str in input_file:
    # this next "for" is not going to work quite the way you think
    # line_str will be an entire line from the file
    # if you loop as you did below, you do not get words, but characters
    # (you can see that with the first loop in the letter_count function)
    # not this -> "for word in line_str:", but this...
    # the split function will look for spaces and split the string there
    line_as_words = line_str.split()
    for word in line_as_words:
        word = clean_word(word)
        # as I mentioned above, don't call wordd here
        #letters = wordd()
        # the reason you were getting an error about dictionaries being "callable"
        # is because you were using the same name for two things
        # you used letter_count above as a function and then here as a variable.
        # I've changed it.
        letters = letter_count(letters, word)
print(letters, file=output_file)

print(f"{letters}")
input_file.close()
output_file.close()
