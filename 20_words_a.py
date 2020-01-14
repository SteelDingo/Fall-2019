def clean_word(word):
    return word.strip().lower()

def line_count(line_as_words, word):
    count = 0
    for word in line_as_words:
        count = count + 1
        if count < 5:
            print(word)
        else:
            print(word + "\n")
            count = 0
    return


input_file = open("20words.txt","r")
output_file = open("4x5words.txt","w")

for line_str in input_file:
    line_as_words = line_str.split()
    for word in line_as_words:
        word = clean_word(word)
new_file = line_count(line_as_words, word)
print(new_file, file=output_file)

print(f"The new file looks like: {new_file}")
input_file.close()
output_file.close()
