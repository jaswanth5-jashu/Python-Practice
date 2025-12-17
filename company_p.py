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


n = [1,2,3]
r = 0
for i in range(len(n)):
    r = r*10+n[i]
r+=1
print([int(i) for i in str(r)])
'''
'''
Question 1: Hidden Number Sum Extraction

Companies test your ability to extract patterns from messy data.

You are given a string S containing letters and digits.
Your task is to extract every continuous sequence of digits, convert them into integers,
and find their total sum.

Rules

A number is formed only by consecutive digits (0-9)

Leading zeros must be ignored (0045 → 45)

If no digits exist, return 0

Sample Input
a10b20c0015x5

Sample Output
50

s = "a100b20c0015x5"
sub = ''
total = 0
for i in s:
    if i.isdigit():
        sub+=i
    elif sub !='':
        total += int(sub)
        sub = ''
total += int(sub)
print(total)
'''
'''
def func(a,b):
    print(a<<b-1)
func(2,5)
'''
'''
Question 2: Depth Balanced Bracket Validator

This version is used in Infosys SP & TCS Digital.

You are given a string containing brackets:
{ } [ ] ( )

A string is balanced ONLY IF:

Every opening bracket has a matching closing bracket

Nesting must be correct (([]) is valid, ([)] is invalid)

Closing bracket must match type ( [ with ] )

String may contain 0 or more characters
'''
'''
s = '{([])}'
d = {'{':'}','(':')','[':']'}
l = []
for i in s:
    if i in d:
        l.append(i)
for x,y in d.items():
    if x in l:
        if y in s:
            l.remove(x)
if len(l) == 0:
    print("yes")
else:
    print("no")
'''
'''
Question 3: Alternate Sorting (Odd & Even Positions)

Given an array A, perform custom sorting:

Sort values at EVEN indices in descending order

Sort values at ODD indices in ascending order

(0-based indexing)

Sample Input
6
4 1 7 3 9 2

Sample Output
[9,1,7,2,4,3]

n = [4,1,7,3,9,2]
even = sorted(n[::2],reverse=True)
odd = sorted(n[1::2])
print(even)
print(odd)
res = []
for i in range(len(even)):
    res.append(even[i])
    res.append(odd[i])
print(res)
'''
'''
5) "Special Array Sum"

Given an array, sum only those elements which satisfy:

Number is prime

AND its index is even

Index is 0-based.

Example

Input:

[3, 4, 5, 6, 7, 8]


Output:

3 + 5 + 7 = 15
'''
n = [3,4,5,6,7,8,13]
s = 0
for d in range(len(n)):
    if d%2 == 0:
        for i in range(2,(d//2)+1):
            if n[d]%i == 0:
                break
        else:
            s = s+n[d]
print(s)