#1
s ="programming"
j  =0
for i in s:
    if i in 'aeiouAEIOU':
        j += 1
print(j) #output: 3

#2
i = len(s)-1
while i<=0:
    if s[i] in 'aeiouAEIOU':
        j = j+1
        i = i-1
print(j)

#3
j = 0
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        j = j+1
print(j) #output: 3

#4
print(sum(1 for i in s if i in 'aeiouAEIOU' ))

#5
x = filter(lambda i: i in 'aeiouAEIOU',s)
print(len(list(x)))

 
