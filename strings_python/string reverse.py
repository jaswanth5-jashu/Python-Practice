#1
s = 'madam'
print(s[::-1])  # Output: madam

#2
s = 'hello'
print([s[i] for i in range(len(s)-1,-1,-1)])

#3
res = ''.join(reversed(s))
print(res)  # Output: olleh

#4
i=len(s)-1
x = ''
while i>=0:
    x = x+s[i]
    i=i-1
print(x)   #output: olleh

#5
def rev(s):
    rev =''
    for i in s:
        rev = i+rev
    print(rev)

rev('okokokok') #output: kokokoko
 