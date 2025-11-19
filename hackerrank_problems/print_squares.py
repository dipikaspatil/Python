"""
Problem: Print Squares

The provided code stub reads an integer, n, from STDIN. 
For all non-negative integers i, print i^2 (the square of i).

Input:
A single integer n.

Output:
Print the square of each non-negative integer less than n on a separate line.

Example:
Input: 3
Output:
0
1
4
"""

# --------------------------
# Solution
# --------------------------

# Read input
n = int(input().strip())

# Loop through all non-negative integers less than n
for i in range(n):
    print(i ** 2)

