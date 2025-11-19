"""
Problem: Weird / Not Weird

Given an integer n, perform the following conditional actions:

- If n is odd, print "Weird"
- If n is even and in the inclusive range 2 to 5, print "Not Weird"
- If n is even and in the inclusive range 6 to 20, print "Weird"
- If n is even and greater than 20, print "Not Weird"

Input: A single integer n
Output: Print "Weird" or "Not Weird"
Constraints: 1 <= n <= 100
Example:
    Input: 3
    Output: Weird
"""

# --------------------------
# Solution
# --------------------------

n = int(input().strip())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:  # n is even and > 20
    print("Not Weird")

