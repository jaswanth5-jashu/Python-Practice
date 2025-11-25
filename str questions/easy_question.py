#1)Find the length of a string without using len() function.
#Example Input:hello world | Example Output:11
'''
s = 'hello world'
c = 0
for i in s:
    c = c+1
print(c)
'''
#Q2) Count how many vowels are in a string.Vowels: a, e, i, o, u (both uppercase + lowercase)
#Example Input: Programming | Example Output:3
'''
#in oops
class Vowels:
    def __init__(self,sen):
        self.sen = sen
    def countvowels(self):
        c = 0
        for i in self.sen:
            if i in 'aeiouAEIOU':
                c+=1
        return c
    
obj = Vowels('programming')
print(obj.countvowels())
'''

#Q3) Reverse a string without using slicing ([::-1]).
# Example Input:hello | Example Output:olleh
'''
s = 'hello'
j = ''
for i in s:
    j = i+j
print(j)

----------------------------------

s = 'hello'
c = ''
for i in range(len(s)-1,-1,-1):
    c = c+str(s[i])
print(c)
'''

#Q4) Count how many times each character appears in a string (loop only, no Counter).
#Example Input: banana | Example Output:
#b : 1
#a : 3
#n : 2
'''
s = 'banana' 
j = ''
for i in s:
    if i not in j:
        print(i,':',s.count(i))
        j=j+i
        
#dict model     
s = 'banana'
j = {}
for i in s:
    if i in j:
        j[i]+=1
    else:
        j[i]=1
for k,v in j.items():
    print(k,':',v)

#---------------------------
j={}
for i in s:
    j[i]=j.get(i,0)+1
    
for k,v in j.items():
    print(k,':',v)


#lambda
s = 'banana'
for i in set(s):
    print(i,':',len(list(filter(lambda x:x == i,s))))
'''

#Find the first repeated character in a string (loop only, no count()).
#Example Input: abcadef | Example Output: a
'''
s = 'abcadef'
char = []

for i in s:
    if i in char:
        print(i)
        break
    char.append(i)

#---------------------------

for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            print(s[i])
            quit()            

#---------------------------

x = {}
for i in s:
    if i in x:
        print(i)
        break
    x[i]=1
'''

#Q6) Find the first NON-repeated character in a string.
#Example Input: aabbcdeff | Example Output: c

'''
s = 'aabbcdeff'

for i in range(len(s)):
    r = False
    for j in range(len(s)):
        if i!=j and s[i] == s[j]:
            r = True
            break
    if not r:
        print(s[i])
        break
#-------------------------------
   
d = {}

for i in s:
    d[i] = d.get(i,0)+1

for i in s:
    if d[i] == 1:
        print(i)
        break
'''

#7) Remove all duplicate characters from a string but keep FIRST occurrence only.
#Example Input: banana | Example Output: ban

'''
s = 'banana'
x = ''
for i in s:
    if i not in x:
        x+=i
print(x)
'''
#8)Remove all special characters from a string (keep only letters & digits).
#Example Input: he!!o@123#wor$ld | Example Output: heo123world

'''
s = 'he!!o@123#wor$ld '
x = ''

for i in s:
    if i.isalnum() == True:
        x = x + i
print(x)

#----------------------------------------------------------

s = 'he!!o@123#wor$ld'
x = ''
for i in s:
    if ('A'<=i<='Z') or ('a'<=i<='z') or ('0'<=i<='9'):
        x = x+i
print(x)
'''

#Q9) Check if two strings are anagrams of each other (without using sorted()).
#Example Input:s1 = "listen"s2 = "silent" | Example Output: True

'''
s = "listen"
s2 = "silent"

a = False
if len(s) != len(s2):
    print(False)
else:
    a = True
    for i in s:
        if s.count(i) != s2.count(i):
            a = False
print(a)

#------------------------------------------

d = {}
d1 = {}

for i in s:
    d[i] = d.get(i,0)+1
for j in s2:
    d1[j] = d1.get(j,0)+1

print(d == d1)
'''

#Q10) Find the vowel count and consonant count in a string (ignore spaces & special characters).
#Example Input: "Hello World!" | Example Output: Vowels: 3 Consonants: 7

s = 'Hello World!'
vowels = 0
con = 0

for i in s:
    if i in 'aeiouAEIOU':
        vowels+=1
    else:
        if i.isalpha() == True:
            con+=1
print(vowels)
print(con)

v = 0
c = 0
for i in s:
    if ('A'<=i<='Z') or ('a'<=i<='z'):
        if i in 'aeiouAEIOU':
            v+=1
        else:
            c+=1
print(v)
print(c)
        