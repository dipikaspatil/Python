"""
HackerRank Problem: Mutations

We have seen that lists are mutable (they can be changed), 
and tuples are immutable (they cannot be changed).

Strings in Python are also immutable, so you cannot modify them directly like:
    string[5] = 'k'   # ❌ Not allowed

Approaches to modify a string:
1. Convert string to list → modify → join back.
2. Slice string around the index and insert new character.

Task:
Read a given string, change the character at a given index, 
and return the modified string.

Function Description:
---------------------
mutate_string(string, position, character)

Parameters:
- string: original string
- position: index where new character should be placed
- character: the new character

Returns:
- New modified string

Sample:
-------
Input:
abracadabra
5 k

Output:
abrackdabra
"""

def mutate_string(string, position, character):
    # Method: slicing (clean and efficient)
    return string[:position] + character + string[position + 1:]


if __name__ == "__main__":
    s = input()
    pos, char = input().split()
    pos = int(pos)
    
    result = mutate_string(s, pos, char)
    print(result)

