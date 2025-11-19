"""
HackerRank Problem: Second Lowest Score

Task:
Given names and grades of students, print the name(s) of the student(s)
with the second lowest grade. If multiple students have the second lowest
score, print their names in alphabetical order.

Input:
First line: integer n (number of students)
Next 2*n lines: name followed by grade

Output:
Names of student(s) with the second lowest grade, each on a new line.

Example:
Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Output:
Berry
Harry
"""

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = sorted(set([s[1] for s in students]))
    second_lowest = scores[1]

    result = sorted([s[0] for s in students if s[1] == second_lowest])

    for name in result:
        print(name)

