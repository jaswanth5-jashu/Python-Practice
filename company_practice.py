'''
Question 1 — "Energy Consumption Analyzer"

Many companies monitor daily machine activity to find inefficiency.
You are given a list of energy readings of a machine taken every hour.
However, some readings are faulty: any reading that is lower than 0 or greater than 1000 is considered invalid and must be removed.

After removing all invalid readings, calculate the average of the remaining valid readings.
If no valid readings exist, print "NO DATA".

Input Format

First line: an integer N (number of readings)

Second line: N space-separated integers (the energy readings)

Output Format

A single value: average of valid readings (rounded down)

Or "NO DATA" if all readings are invalid

Sample Input
8
200 300 -5 1200 450 600 0 50

Sample Output
266

Explanation

Valid readings = 200, 300, 450, 600, 0, 50
Average = 1600 / 6 = 266.66 → round down → 266

N = [200,300,-5,1200,450,600,0,50]
total = 0
c = 0
for i in N:
    if 0<=i<=1000:
        c+=1
        total+=i
if c == 0:
    print('NO data')
print(total//c)      
'''
'''     
Question 2 — "Customer Queue Simulation"

A store records customers entering (E) and leaving (L).
You must simulate the queue and determine the maximum number of customers present at any moment.

Rules:

Each E increases customer count by 1

Each L decreases customer count by 1

Customer count will never go below 0

At least 1 event will be given

Input Format

A string consisting only of 'E' and 'L'.

Output Format

An integer: max customers at any time

Sample Input
EELEELLE

Sample Output
3


c = 0
ma = 0
n = input('enter coustamer status E/L :')
for i in n:
    if i == 'E':
        c+=1
    else:
        c-=1
    if c<0:
        c = 0
    if c>ma:
        ma = c
print(ma)
'''
'''
Question 3 — "String Rewriting Rule"

You are given a string S.
If a character repeats 3 or more times consecutively, replace that whole sequence with a single instance of that character followed by the count.

Example: "aaabb" → “a3bb”.

If no such sequences exist, print the string as is.

Input Format

A single string S (only lowercase letters).

Output Format

A transformed string according to rules.

Sample Input
aaabccccdd

Sample Output
a3bc4dd

s = input('enter string :')
i = 0
res = ''
while i<len(s):
    c = 1
    while i+1<len(s) and s[i] == s[i+1]:
        c+=1
        i+=1
    if c>=3:
        res+=s[i]+str(c)
    else:
        res+=s[i]*c
    i+=1
print(res)
'''

'''
Question 4 — "Unique Product IDs"

A warehouse stores product IDs in a list.
Your job is to remove:

All duplicate IDs

All IDs that are negative

All IDs that are greater than 5000

After cleaning, print the remaining IDs in ascending order.
If no IDs remain, print "EMPTY".

Input Format

N

N space-separated integers

Output Format

Cleaned list of product IDs (space-separated)

Sample Input
7
300 50 300 -2 7000 12 50

Sample Output
12 50 300

x = [300,50,300,-2,7000,12,50]
y = sorted(set(x))
res = []
for i in y:
    if 0<=i<=5000:
        res.append(i)
if len(res) == 0:
    print('EMPTY')
else:
    print(res)
'''
'''
Question 5 — "Task Completion Time"

A worker completes tasks with known durations.
Given a target time T, find how many smallest-duration tasks can be finished without exceeding time T.

Input Format

N

N space-separated integers (task times)

T (max total time)

Output Format

Maximum number of tasks

Sample Input
5
4 2 8 1 3
7

Sample Output
3

Explanation

Smallest tasks = 1, 2, 3 → total = 6 ≤ 7 → 3 tasks

x = [4,2,8,1,3]
y = sorted(x)
m = 7

t=0
c = 0
for i in y:
    if t+i<=m:
        t+=i
        c+=1
print(c)
'''

#--------------------------------------------------------
'''
Problem 1 — “Character Frequency Compression”

You are given a string S consisting of lowercase letters.
You must compress it by counting how many times each character appears in the entire string.

BUT output must be in sorted order of characters.

Input
bbbaaaccd

Output
a3b3c2d1


s = "bbbaaaccd"
res = sorted(s)
r = ''
i = 0
while i<len(res):
    c = 1
    while i+1<len(res) and res[i] == res[i+1]:
            c+=1
            i+=1
    r = r+res[i]+str(c)
    i+=1
print(r)
'''
'''
Problem 2 — “Even-Odd Sum Checker”

Given a list of integers, find:

Sum of even numbers

Sum of odd numbers

If even sum > odd sum, print "EVEN"
If odd sum > even sum, print "ODD"
If equal, print "EQUAL".

Input
7
1 2 3 4 5 6 7

Output
ODD


x = [1,2,3,4,5,6,7]
even = [i for i in x if i%2 ==0]
odd = [j for j in x if j%2 !=0]

if sum(even)>sum(odd):
    print('EVEN')
else:
    print('ODD')
'''
'''
Problem 3 — “First Non-Repeating Character”

You are given a string S.
Find the first character that does NOT repeat anywhere in the string.
If all characters repeat, print -1.

Input
aabbcdde

Output
c

s = "aabbcdde"
for i in range(len(s)):
    if s.count(s[i]) == 1:
        print(s[i])
        break
'''
'''
Problem 4 — “Count Unique Pairs With Sum K”

Given an array and a value K, count unique pairs (a, b) such that:

a + b = K


Pairs must be unique → (2,5) and (5,2) are same → count ONCE.

Input
N = 6
arr = 1 5 7 -1 5 2
K = 6

Output
2
'''
#-----------------------------------------------------------------------------------------
'''
Q2. Find character frequency but print only characters that appear more than once.
Input: "programming"
Output: {r:2, g:2, m:2}

s = "programming"
d = {}
for i in s:
    if s.count(i) >= 2:
        d[i] = d.get(i,0)+1
print(d)
'''
'''
Q3. Merge two dictionaries but if a key collides, store values in a list.
Input: {'a':10, 'b':20}, {'b':5, 'c':40}
Output: {'a':10, 'b':[20,5], 'c':40}

s = {'a':10, 'b':20}
s1 = {'b':5, 'c':40}
for k,v in s1.items():
    if k in s:
        if type(s[k]) == list:
            s[k].append(v)
        else:
            s[k] = [s[k],v]
    else:
        s[k]= v
print(s)
'''
'''
2️⃣ List / Tuple / Set

Q4. Move all zeros to the end without using extra list.
Input: [0,2,0,5,0,3]
Output: [2,5,3,0,0,0]

l = [0,2,0,5,0,3]
w = 0
for i in range(len(l)):
    if l[i] !=0:
        l[w] = l[i]
        w+=1
for i in range(w,len(l)):
    l[i] = 0
print(l)
'''

s = 'abcdabcdd'
l = ''
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub = s[i:j]
        
        if len(sub)>len(l):
            l = sub
print(l)
        
        
    