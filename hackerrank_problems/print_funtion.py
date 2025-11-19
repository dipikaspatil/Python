"""
Problem: Print Consecutive Numbers

Task:
The included code stub reads an integer n from STDIN.
Without using any string methods, print the consecutive integers from 1 through n, all on the same line, without spaces.

Input Format:
A single integer n.

Output Format:
Print the numbers from 1 to n as a single string (no spaces).

Sample Input 0:
3

Sample Output 0:
123
"""

# --------------------------
# Solution
# --------------------------

if __name__ == "__main__":
    n = int(input().strip())
    
    # Loop through numbers 1 to n and print them on the same line
    for i in range(1, n + 1):
        print(i, end='')  # end='' avoids spaces or newlines
    print()  # optional: print newline at the end

# --------------------------
# Test Cases (Optional)
# --------------------------
# Input: 3 -> Output: 123
# Input: 5 -> Output: 12345
# Input: 1 -> Output: 1

