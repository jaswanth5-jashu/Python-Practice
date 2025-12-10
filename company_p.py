'''
Question 1 — Increment the digit array

You are given an array of digits representing a non-negative integer.
Increment the integer by 1 and return the result as an array.

Input
[1,2,3]

Output
[1,2,4]

Another
[9]

Output
[1,0]
'''

n = [1,2,3]
r = 0
for i in range(len(n)):
    r = r*10+n[i]
r+=1
print([int(i) for i in str(r)])

