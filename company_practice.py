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
