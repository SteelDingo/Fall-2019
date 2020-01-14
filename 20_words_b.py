def clean_word(word):
    return word.strip().lower()

def line_count(line_as_words, output_file):
    count = 0
    for word in line_as_words:
        count = count + 1
        if count < 5:
            print(word, end=" ", file=output_file)
        else:
            print(word, end="\n", file=output_file)
            count = 0

input_file = open("20words.txt","r")
output_file = open("4x5words.txt","w+")

for line_str in input_file:
    line_as_words = line_str.split()
# these next two lines really don't do much for you. You're not updating "line_as_word"
# what you're doing is updating "word", but you don't save the result anywhere so this
# is doing nothing
    # for word in line_as_words:
    #     word = clean_word(word)
line_count(line_as_words, output_file)

print(f"A new file named 4x5words.txt was created.")
for line in output_file:
    #line_str = line
    print(f"{line}")
input_file.close()
output_file.close()
