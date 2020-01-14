import random

print("Wheel of Fortune!")
word_raw = input("Enter a word: \n")
word = str.upper(word_raw)

word_so_far = list(' ' * len(word))

guessed_so_far = ''

P1 = input("Player 1: \n")
P2 = input("Player 2: \n")
P3 = input("Player 3: \n")
Players = [P1, P2, P3]

Bank = [0, 0, 0]

flag = True

def spin(input):
    score = random.randint(1,30)
    return score*100

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
    return guessed

def solve(solve_guess):
    if solve_guess == word:
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
        while turn:
            choice = input("Would you like to spin, buy a vowel, or solve?\n")
            ch = str.lower(choice)
            if ch=="spin":
                spin_f = spin(input)
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
                            word_so_far[letter_index] = guess
                else:
                    print(f"Sorry, there are no {guess}'s.")
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
                    string_so_far = "".join(word_so_far)
                    print(f"The word to guess |{string_so_far}|")
                    print(f"You guessed {solve_guess}.")
                    print(f"Sorry, that's incorrect.")
                    print(f"Current score: {Bank[player_index]}")
                    turn = False
                else:
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
