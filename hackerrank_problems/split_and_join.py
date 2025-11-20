"""
HackerRank Problem: Split and Join

Task:
You are given a string. Split the string on a space (" ") delimiter and then join the resulting list using a hyphen ("-").

Example:
Input:  "this is a string"
Output: "this-is-a-string"

Function Description:
Complete the split_and_join function below.

split_and_join has the following parameter:
- string line: a string of space-separated words

Returns:
- string: the resulting hyphen-joined string

------------------------------------------
Explanation:
------------------------------------------
In Python, splitting and joining strings is straightforward:

1. Splitting:
   line.split(" ")
   - Splits the string into a list wherever a space is found.
   Example:
     "this is a string" -> ["this", "is", "a", "string"]

2. Joining:
   "-".join(words)
   - Joins list elements into a single string using the hyphen as the separator.
   Example:
     ["this", "is", "a", "string"] -> "this-is-a-string"

The problem simply combines these two steps.
"""

# Function to split by space and join by hyphen
def split_and_join(line):
    words = line.split(" ")        # Step 1: split by spaces
    return "-".join(words)         # Step 2: join with hyphens

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

