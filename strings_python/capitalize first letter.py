#1
s = 'raki'
print(s.capitalize())  # Output: Raki

#2
s = 'python programming'
print(s[0].upper()+s[1:]) # Output: Python programming  

#3
s = 'bahubali'
res = ''
for i in range(len(s)):
    if i == 0:
        r = chr(ord(s[i])-32)
        res = res + r
print(res+s[1:])


