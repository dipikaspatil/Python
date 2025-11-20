"""
HackerRank Problem: Tuple and Hash

Task:
Given an integer n and n space-separated integers, create a tuple of those integers.
Compute and print the hash of the tuple.

Input Format:
1. First line: integer n — number of elements in the tuple
2. Second line: n space-separated integers

Output Format:
Print the result of hash(t) where t is the tuple of integers.

Note:
- hash() is a built-in function in Python.
- Only immutable objects (like tuple) can be hashed.
- Lists cannot be hashed since they are mutable.
- Hash values for tuples may differ between Python versions or sessions due to hash randomization.
  Hackerrank uses PyPy 3 which produces fixed hash values for testing.

Sample Input:
2
1 2

Sample Output (on Hackerrank/PyPy 3):
3713081631934410656
"""

if __name__ == '__main__':
    n = int(input())
    nums = map(int, input().split())

    t = tuple(nums)          # convert list of integers to tuple
    print(hash(t))           # print hash value of the tuple

"""
Hash Information:
-----------------
- hash() returns an integer representing the hash value of an object.
- Tuples can be hashed because they are immutable.
- The hash is used internally in data structures like dictionaries and sets.
- Python computes a tuple's hash by combining the hashes of its individual elements.
- The combination uses a special algorithm (primes and bit operations) to produce a single integer.
- Changing the order or values of elements changes the hash.
- Tuples with the same elements in the same order have the same hash within a Python session.
- Hash values may differ across Python versions or program executions due to hash randomization.
- Hackerrank uses PyPy 3 to ensure fixed hash outputs for testing.

Analogy:
Think of the hash as a compressed fingerprint of the tuple:
- (1, 2) -> fingerprint integer A
- (2, 1) -> fingerprint integer B (different)
- Python uses this fingerprint internally for quick dictionary/set lookups.
"""

