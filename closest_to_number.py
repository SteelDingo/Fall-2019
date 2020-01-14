import random
number = random.randint(0,100)

print("I'm thinking of a number between 1 and 100...")
print()

P1_guess = int(input("Player 1, guess: \n"))
P2_guess = int(input("Player 2, guess: \n"))

#P1_abs = abs(P1_guess)
#P2_abs = abs(P2_guess)

P1_result = abs(number - P1_guess)
P2_result = abs(number - P2_guess)

if P1_result < P2_result:
    print(f"Player 1 wins! Their guess was closer to {number} than Player 2.")
elif P2_result < P1_result:
    print(f"Player 2 wins! Their guess was closer to {number} than Player 1.")
elif P1_result == number:
    print(f"Player 1 wins! They guessed the number, which was {number}.")
elif P2_result == number:
    print(f"Player 2 wins! They guessed the number, which was {number}.")
elif P1_result == P2_result:
    print(f"It's a tie! The number was {number}.")
