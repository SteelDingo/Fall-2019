# build the dictionary

# no inputs
# this function will return a dictionary
def init_dict():
    # first an empty dictionary
    letters = {}

    # now we want to add a key-value pair for each letter in the alphabet
    # the alphabet has 26 letters.
    # If I knew how to write a loop over the letters of the alphabet directly, I would
    # since I don't I use this integer index
    for index in range(26):
        # Next we calculate the "key" which is the letter of the alphabet
        # The index starts at zero and goes to 25
        # to get this thing to produce an "a" as the first letter, I use ord to get it's ordinal value
        # Then I add the index ('a'+0 = 'a', 'a'+1 = 'b', etc)
        key = chr(ord('a')+index)
        # now that we have the key, we'll add the key to the dictionary and set its value to zero
        # we start with zero since we've not seen any letters yet
        letters[key] = 0
    return letters


# we have to pass the dictionary and the word since we want to deal with local variables only
# this function will return the dictionary after updating the counts therein
# assuming word is lower case already
def letter_count(letters, word):
    # let's loop over all the letters in this new word
    for ch in word:
        # we're told to ignore non-letters
        # this statement asks if "ch" is already a key in the dictionary
        if ch in letters:
            # since the character is in the letters dictionary, it must be a...z
            # now we use the index function "[]" to find the appropriate dictionary entry and increment the count
            letters[ch] = letters[ch] + 1
    return letters




