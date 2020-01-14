#define functions that are used below
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def spin(input):
    import random
    score = random.randint(1,30)
    return score*100

def check_guess(input):
    for ch in input:
        if ch in Alphabet=='A''E''I''O' or 'U':
            return print("You have to buy a vowel.")
        else:
            return print("You guessed {ch}.")

def vowel():
    pass

def solve():#solve function
    pass

print("Wheel of Fortune!")
word_raw = input("Enter a word: \n")
word = str.upper(word_raw)
#convert word to uppercase for display purposes

P1 = input("Player 1: \n")
P2 = input("Player 2: \n")
P3 = input("Player 3: \n")
Players = [P1, P2, P3]
#player names
flag = 1
#set flag to 0 when puzzle is solved
#Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while flag:
    for player in Players:
        print(f"{player}'s turn.")
        turn = True
        #set to False when turn over
        while turn:
            choice = input("Would you like to spin, buy a vowel, or solve?\n")
            ch = str.lower(choice)
            if ch=="spin":
                spin_f = spin(input)    # here you call the spin function. you define it above
                print(f"Spun {spin_f}.")
                guess = input("Guess a letter:\n")
                guess_upper = guess.upper()
                check_guess = check_guess(guess_upper)
                
                #letter_1 = input("Guess a letter:\n")
                #letter = str.upper(letter_1)
                #for letter in letters:
                    #if letter=="A,E,I,O,U":
                        #print("You have to buy a vowel.")
                    
                turn = False
            elif ch=="buy a vowel":
                vowel()
                turn = False
            elif ch=="solve":
                solve()
                turn = False
            else:
                print("Pick one of the three options.")

