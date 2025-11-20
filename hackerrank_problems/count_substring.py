"""
Problem:
--------
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs 
in the given string. String traversal takes place from left to right.

NOTE: The letters are case-sensitive.

Example:
--------
Input:
ABCDCDC
CDC

Output:
2

Concept:
--------
- len(s) gives the length of a string.
- You can loop through a string using:

    for i in range(0, len(s)):
        print(s[i])

- range(0, 5) loops from 0 to 4.

Approach:
---------
We slide over the string and compare each slice of length len(sub) 
with the substring. If they match, we increase the count.

"""

def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)

    for i in range(len(string) - sub_len + 1):
        if string[i:i + sub_len] == sub_string:
            count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    result = count_substring(string, sub_string)
    print(result)

