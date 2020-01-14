import random

print("Wheel of Fortune!")
word_raw = input("Enter a word: \n")
word = str.upper(word_raw)

# NOTE: This is where we'll populate the letters that are correctly guessed
# If you did not learn this syntax, please let me know.
# NOTE: strings are immutable so I have to use a list here
word_so_far = list(' ' * len(word))

# NOTE: This is were we record the letters guessed so far.
guessed_so_far = ''

#convert word to uppercase for display purposes

P1 = input("Player 1: \n")
P2 = input("Player 2: \n")
P3 = input("Player 3: \n")
Players = [P1, P2, P3]
#player names

# NOTE: Used to track winnings so far
Bank = [0, 0, 0]

flag = True
#set flag to 0 when puzzle is solved

#define functions that are used below
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# NOTE: you're not using "input" here, so don't pass it.
def spin(input):
    score = random.randint(1,30)
    return score*100

# NOTE: after a spin, the user can pick one character
def is_vowel(ch):
    if ch in 'AEIOU':
        return True
    else:
        return False

def vowel(vwl, player_index):
    guessed = ''
    if vwl in word:
        count = 0
        for letter_index in range(len(word)):
            if vwl == word[letter_index]:
                count = count + 1
        if Bank[player_index] >= (count * 250):
            for letter_index in range(len(word)):
                if vwl == word[letter_index]:
                    Bank[player_index] = Bank[player_index] - 250
                    word_so_far[letter_index] = vwl
                    guessed = vwl
        else:
            print(f"Sorry, you do not have enough money.")
    else:
        print(f"Sorry, there are no {vwl}'s.")
    # string_so_far = "".join(word_so_far)
    # print(f"The word to guess |{string_so_far}|")
    # print(f"The letters guessed include: {guessed_so_far}")
    # print(f"Current score: {Bank[player_index]}")
    return guessed

def solve(solve_guess):
    #s_guess = len(solve_guess)
    if solve_guess == word:
        #flag = False
        return True
    else:
        return False

solution = False

while flag:
    for player_index in range(len(Players)):
        player = Players[player_index]
        print(f"{player}'s turn.")
        if solution==False:
            turn = True
        else:
            turn = False
        #set to False when turn over
        while turn:
            choice = input("Would you like to spin, buy a vowel, or solve?\n")
            ch = str.lower(choice)
            if ch=="spin":
                spin_f = spin(input)    # here you call the spin function. you define it above
                print(f"Spun {spin_f}.")
                beenGuessed = True
                gotVowel = True
                while beenGuessed:
                    while gotVowel:
                        guess = input("Guess a letter:\n")
                        guess = guess.upper()
                        gotVowel = is_vowel(guess)
                        if gotVowel:
                            print(f"You picked a vowel. Please pick a consonant.")
                    if guess in guessed_so_far:
                        gotVowel = True
                        print(f"Someone has guessed that letter. Please pick a different letter.")
                    else:
                        beenGuessed = False
                        guessed_so_far = guessed_so_far + guess
                if guess in word:
                    for letter_index in range(len(word)):
                        if guess == word[letter_index]:
                            Bank[player_index] = Bank[player_index] + spin_f
                            bank = Bank[player_index]
                            print(f"Current score: {bank}")
                           # Increase the bank account by spin_f for this player
                           # keep track of the letters guessed in the word order
                            word_so_far[letter_index] = guess
                else:
                    print(f"Sorry, there are no {guess}'s.")
                    #print(f"Current score: {bank}")
                string_so_far = "".join(word_so_far)
                print(f"The word to guess |{string_so_far}|")
                print(f"The letters guessed include: {guessed_so_far}")


                turn = False
            elif ch=="buy a vowel":
                buyVowel = False
                gotVowel = False
                while not buyVowel:
                    vwl = input("What vowel would you like to buy?\n")
                    vwl = vwl.upper()
                    buyVowel = is_vowel(vwl)
                    if buyVowel==False:
                        print("You picked a consonant. Please pick a vowel.")
                    #while not gotVowel:
                        #if vwl in guessed_so_far:
                            #gotVowel = False:
                            #print(f"Someone has guessed that letter. Please pick a different letter.")
                guessed_so_far = guessed_so_far + vowel(vwl, player_index)
                string_so_far = "".join(word_so_far)
                print(f"The word to guess |{string_so_far}|")
                print(f"The letters guessed include: {guessed_so_far}")
                print(f"Current score: {Bank[player_index]}")

                turn = False

            elif ch=="solve":
                solve_guess = input("Solve the puzzle:\n")
                solve_guess = solve_guess.upper()
                solution = solve(solve_guess)
                if solution==False:
                    #word_so_far = word_so_far[letter_index]
                    string_so_far = "".join(word_so_far)
                    print(f"The word to guess |{string_so_far}|")
                    print(f"You guessed {solve_guess}.")
                    print(f"Sorry, that's incorrect.")
                    print(f"Current score: {Bank[player_index]}")
                    turn = False
                else:
                    #word_so_far = word_so_far[letter_index]
                    string_so_far = "".join(word_so_far)
                    print(f"The word to guess |{string_so_far}|")
                    print(f"You guessed {solve_guess}.")
                    print(f"The word is: {word}")
                    print(f"Congratulations! You win!")
                    print(f"Your score: {Bank[player_index]}")
                    flag = False
                    turn = False
            else:
                print("Pick one of the three options.")

print(f"{P1}'s score: {Bank[0]}")
print(f"{P2}'s score: {Bank[1]}")
print(f"{P3}'s score: {Bank[2]}")
