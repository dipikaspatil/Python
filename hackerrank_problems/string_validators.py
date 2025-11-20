"""
HackerRank Problem: String Validators

Task:
Given a string s, check if it contains:
1. any alphanumeric characters
2. any alphabetical characters
3. any digits
4. any lowercase characters
5. any uppercase characters

Input Format:
A single line containing a string s.

Output Format:
Print 5 lines, each line with True/False for the checks in the order above.

Approach:
We use Python's `any()` function combined with string methods to check for each property.
"""

if __name__ == "__main__":
    s = input().strip()

    # Check and print directly using any() for concise Pythonic code
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
