def reverse_string(S):
    S1=''
    for c in S:
        S1 = c + S1
    return S1

S = input(str("Type a string: \n"))
S1 = reverse_string(S)
print(f"Reverssed it's: {S1}")
