"""
HackerRank Problem: Swap Case

Task:
Given a string, convert all lowercase letters to uppercase and all uppercase letters to lowercase.
Non-alphabetic characters (numbers, punctuation, spaces) remain unchanged.

Function Description:
Complete the swap_case function below.

swap_case has the following parameter:
- string s: the string to modify

Returns:
- string: the modified string

Sample Input:
HackerRank.com presents "Pythonist 2".

Sample Output:
hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""

def swap_case(s):
    # Use Python's built-in swapcase() method to swap the case of letters
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    print(swap_case(s))

"""
Explanation:
-----------------
- str.swapcase() automatically converts lowercase letters to uppercase and uppercase to lowercase.
- Non-alphabetic characters (numbers, punctuation, spaces) remain unchanged.
- This method handles the problem requirements in a single line efficiently.

Examples:
"Www.HackerRank.com" -> "wWW.hACKERrANK.COM"
"Pythonist 2" -> "pYTHONIST 2"
"""
