print("Wheel of Fortune!")
word_raw = input("Enter a word: \n")
word = str.upper(word_raw)
#convert word to uppercase for display purposes

P1 = input("Player 1: \n")
P2 = input("Player 2: \n")
P3 = input("Player 3: \n")
#player names
flag = 1
#set flag to 0 when puzzle is solved

while flag:
    print(f"{P1}'s turn.")
    P1_turn = True
    #set to False when turn over
    while P1_turn:
        P1_choice = input("Would you like to spin, buy a vowel, or solve?\n")
        P1_ch = str.lower(P1_choice)
        if P1_ch=="spin":
            def spin():#spin function
                pass
            P1_turn = False
        elif P1_ch=="buy a vowel":
            def vowel():#vowel function
                pass
            P1_turn = False
        elif P1_ch=="solve":
            def solve():#solve function
                pass
            P1_turn = False
        else:
            print("Pick one of the three options.")

    print(f"{P2}'s turn.")
    P2_turn = True
    while P2_turn:
        P2_choice = input("Would you like to spin, buy a vowel, or solve?\n")
        P2_ch = str.lower(P2_choice)
        if P2_ch=="spin":
            def spin():#spin function
                pass
            P2_turn = False
        elif P2_ch=="buy a vowel":
            def vowel():#vowel function
                pass
            P2_turn = False
        elif P2_ch=="solve":
            def solve():#solve function
                pass
            P2_turn = False
        else:
            print("Pick one of the three options.")

    print(f"{P3}'s turn.")
    P3_turn = True
    while P3_turn:
        P3_choice = input("Would you like to spin, buy a vowel, or solve?\n")
        P3_ch = str.lower(P3_choice)
        if P3_ch=="spin":
            def spin():#spin function
                pass
            P3_turn = False
        elif P3_ch=="buy a vowel":
            def vowel():#vowel function
                pass
            P3_turn = False
        elif P3_ch=="solve":
            def solve():#solve function
                pass
            P3_turn = False
        else:
            print("Pick one of the three options.")
        
