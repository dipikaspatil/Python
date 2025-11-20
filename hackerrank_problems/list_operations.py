"""
Problem: List Operations
------------------------
You are given a series of commands to modify a list. The commands can be:

1. insert i e   -> Insert integer e at position i
2. print        -> Print the list
3. remove e     -> Remove the first occurrence of integer e
4. append e     -> Append integer e to the end
5. sort         -> Sort the list
6. pop          -> Pop the last element
7. reverse      -> Reverse the list

You will receive N commands, and you must execute them in order.
For every 'print' command, output the current list.

Sample Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        command = input().split()
        cmd = command[0]

        if cmd == "insert":
            i = int(command[1])
            e = int(command[2])
            lst.insert(i, e)
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            e = int(command[1])
            lst.remove(e)
        elif cmd == "append":
            e = int(command[1])
            lst.append(e)
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()

