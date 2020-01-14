import random

class player:
    def __init__(self, name):
        self.name = name
        self.winnings = 0

class puzzle:
    def __init__(self, pfile):
        self.pfile = pfile
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def prepare_game(self):
        words=[line.strip() for line in open(words_file)]
        pick=str.upper(random.choice(words))
        self.word = pick
##        print(self.word)                                    # for testing
        self.word_so_far = list(' ' * len(self.word))
        self.guessed_so_far = ''
        self.solved = False

    def spin(self, player):
        score = (random.randint(1,30)*100)
        print(f"Spun {score}.")
        beenGuessed = True
        gotVowel = True
        while beenGuessed:
            while gotVowel:
                self.guess = str.upper(input("Pick a letter:\n"))
                gotVowel = Puzzle.is_vowel()
                if gotVowel:
                    print(f"You picked a vowel. Please pick a consonant.")
            if self.guess in self.guessed_so_far:
                gotVowel = True
                print(f"Someone has guessed that letter. Please pick a different letter.")
            else:
                beenGuessed = False
                self.guessed_so_far = self.guessed_so_far + self.guess
        if self.guess in self.word:
            for letter_index in range(len(self.word)):
                if self.guess == self.word[letter_index]:
                    player.winnings = player.winnings + score
                    print(f"Current score: {player.winnings}")
                    self.word_so_far[letter_index] = self.guess
        else:
            print(f"Sorry, there are no {self.guess}'s.")
        self.string_so_far = "".join(self.word_so_far)
        print(f"The word to guess |{self.string_so_far}|")
        print(f"The letters guessed include: {self.guessed_so_far}")

    def is_vowel(self):
        if self.guess in 'AEIOU':
            return True
        else:
            return False

    def vowel(self, player):
        guessed = ''
        if self.guess in self.word:
            count = 0
            for letter_index in range(len(self.word)):
                if self.guess == self.word[letter_index]:
                    count = count + 1
            if player.winnings >= (count*250):
                for letter_index in range(len(self.word)):
                    if self.guess == self.word[letter_index]:
                        player.winnings = player.winnings - 250
                        self.word_so_far[letter_index] = self.guess
                        guessed = self.guess
            else:
                print("Sorry, you do not have enough money.")
        else:
            print(f"Sorry, there are no {self.guess}'s.")
        return guessed

    def buy_vowel(self, player):
        buyVowel = False
        gotVowel = False
        while not buyVowel:
            self.guess = str.upper(input("Select a vowel:\n"))
            buyVowel = Puzzle.is_vowel()
            if buyVowel==False:
                print("You picked a consonant. Please pick a vowel.")
        self.guessed_so_far = self.guessed_so_far + Puzzle.vowel(Players[player_index])
        self.string_so_far = "".join(self.word_so_far)
        print(f"The word to guess |{self.string_so_far}|")
        print(f"The letters guessed include: {self.guessed_so_far}")
        print(f"Current score: {player.winnings}")

    def get_solution(self):
        if self.solve_guess == self.word:
            return True
        else:
            return False

    def solve(self, player):
        self.solve_guess = str.upper(input("Solve the puzzle:\n"))
        self.solution = Puzzle.get_solution()
        if self.solution==False:
            self.string_so_far = "".join(self.word_so_far)
            print(f"The word to guess |{self.string_so_far}|")
            print(f"You guessed: {self.solve_guess}.")
            print("Sorry, that's incorrect.")
            print(f"Current score: {player.winnings}")
        else:
            self.string_so_far = "".join(self.word_so_far)
            print(f"The word to guess |{self.string_so_far}|")
            print(f"You guessed: {self.solve_guess}.")
            print(f"The word is: {self.word}.")
            print("Congratulations! You win!")
            print(f"Your score: {player.winnings}")
            Puzzle.solved=True



P1 = player(input("Enter a name for player 1: "))
P2 = player(input("Enter a name for player 2: "))
P3 = player(input("Enter a name for player 3: "))
Players = [P1, P2, P3]

words_file = 'words.txt'
Puzzle = puzzle(words_file)
Puzzle.prepare_game()

while not Puzzle.solved:
    for player_index in range(len(Players)):
        if not Puzzle.solved:
            player_name = Players[player_index].name
            player_winnings = Players[player_index].winnings
            print(f"{player_name}'s turn.")
            if Puzzle.solved==False:
                turn = True
            else:
                turn = False
            while turn:
                choice = str.upper(input("Would you like to spin, buy a vowel, or solve?\n"))
                if 'SPIN' in choice:
                   Puzzle.spin(Players[player_index])
                   turn = False
                elif 'BUY A VOWEL' in choice:
                    Puzzle.buy_vowel(Players[player_index])
                    turn = False
                elif 'SOLVE' in choice:
                    Puzzle.solve(Players[player_index])
                    if Puzzle.solved==True:
                        turn = False
                    else:
                        turn = False
                else:
                    print("Pick one of the three options.")

