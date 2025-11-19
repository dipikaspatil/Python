"""
Problem: List Comprehensions with 3D Grid

Task:
You are given three integers x, y, z representing the dimensions of a cuboid, 
and an integer n. Print a list of all possible coordinates [i, j, k] on a 3D grid 
where the sum i + j + k is NOT equal to n. Use list comprehensions.

Input Format:
Four integers x, y, z, n, each on a separate line.

Output Format:
Print the list of coordinates in lexicographic order.

Sample Input:
1
1
1
2

Sample Output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

------------------------------------------------------------
List Comprehension Note:
- List comprehension is a concise way to create lists in Python.
- Syntax: [expression for item in iterable if condition]
- Example: squares = [x**2 for x in range(5)]
- Can handle nested loops: [[i,j] for i in range(3) for j in range(3)]
"""

# --------------------------
# Solution
# --------------------------

if __name__ == "__main__":
    x = int(input().strip())
    y = int(input().strip())
    z = int(input().strip())
    n = int(input().strip())

    result = [[i, j, k] 
              for i in range(x + 1) 
              for j in range(y + 1) 
              for k in range(z + 1) 
              if i + j + k != n]

    print(result)

# --------------------------
# Test Cases (Optional)
# --------------------------
# Input: 1 1 1 2 -> Output: [[0,0,0],[0,0,1],[0,1,0],[1,0,0],[1,1,1]]

