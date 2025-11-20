"""
HackerRank Problem: Finding the Percentage (Average Marks)

Task:
Given a dictionary of student names and their list of marks, print the
average marks for a queried student, formatted to 2 decimal places.

Input Format:
1. First line: integer n — number of student records
2. Next n lines: name followed by their marks
3. Final line: query_name — the student's name to fetch the average for

Output:
Print the average of the marks obtained by the queried student,
correct to 2 decimal places.

Example:
Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Output:
56.00
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *scores = input().split()
        scores = list(map(float, scores))  # convert score strings to floats
        student_marks[name] = scores

    query_name = input()
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg:.2f}")

