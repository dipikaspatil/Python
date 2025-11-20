"""
HackerRank Problem: Print Full Name

Task:
You are given the first name and last name of a person on two separate lines.
Your task is to read them and print the following message:

    Hello <firstname> <lastname>! You just delved into python.

Function Description:
Complete the print_full_name function below.

Parameters:
- first: the first name
- last: the last name

Prints:
A formatted string:
    Hello <first> <last>! You just delved into python.

Sample Input:
Ross
Taylor

Sample Output:
Hello Ross Taylor! You just delved into python.

Explanation:
Python strings support easy formatting using f-strings:
    f"Hello {first} {last}! You just delved into python."
This lets you embed variables directly inside a string.
"""

# Function implementation
def print_full_name(first, last):
    # Using an f-string for clean and readable formatting
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input().strip()
    last_name = input().strip()
    print_full_name(first_name, last_name)

