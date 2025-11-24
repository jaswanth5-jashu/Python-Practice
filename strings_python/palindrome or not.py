#1
s = 'mowabro'
def rev(s):
    re = ''
    for i in s:
        re = i+re
    if s==re:
        print('hahaha')
    else:
        print('damm shit')

rev(s)

#2
x = 'madam'
def ok(x):
    if x == x[::-1]:
        print('jai bahubali')
    else:
        print('dandalu ayya')
ok(x)

#3
j = 'madam'
def mahendra(g):
    if g == ''.join(reversed(g)):
        print('kattapa')
    else:
        print('ballaladeva')

mahendra(j)

#4
f = 'madam'
def bhai(f):
    res = ''
    for i in range(len(f)-1,-1,-1):
        res = f[i]+res
    if f == res:
        print('mahishmathi')
    else:
        print('anushka kota')
bhai(f)
    
 