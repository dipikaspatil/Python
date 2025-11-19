"""
HackerRank Problem: Runner-Up Score

Task:
Given the participants' score sheet, find the runner-up score.
- Input:
    First line: integer n (number of scores)
    Second line: n space-separated integers
- Output:
    Print the second highest unique score.

Example:
Input:
5
2 3 6 6 5
Output:
5
Explanation:
The highest score is 6, runner-up is 5.
"""

# HackerRank Problem: Runner-Up Score
# Reads a list of integers and prints the second highest unique score

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    unique_scores = list(set(arr))      # remove duplicates
    unique_scores.sort()                # sort ascending

    print(unique_scores[-2])            # second last = runner-up

