"""
Problem: Leap Year Check

Task:
Given a year, determine whether it is a leap year.
Return True if it is a leap year, otherwise return False.

Rules (Gregorian calendar):
- If the year is divisible by 4, it is a leap year, unless:
    - It is divisible by 100, then it is NOT a leap year, unless:
        - It is divisible by 400, then it IS a leap year.

Input Format:
A single integer, year.

Output Format:
Return True if leap year, False otherwise.

Sample Input 0:
1990
Sample Output 0:
False

Sample Input 1:
2000
Sample Output 1:
True
"""

# --------------------------
# Solution
# --------------------------

def is_leap(year):
    # One-liner boolean expression for leap year
    leap = year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    return leap

# --------------------------
# Example usage
# --------------------------
if __name__ == "__main__":
    year = int(input().strip())
    print(is_leap(year))

# --------------------------
# Test Cases (Optional)
# --------------------------
# 1990 -> False
# 2000 -> True
# 1900 -> False
# 2400 -> True
# 2100 -> False

