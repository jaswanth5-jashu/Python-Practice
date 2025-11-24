a = [1,2,3,4,5,6,7,8,9,10]
'''
e = [i for i in a if i%2==0]
o = [j for j in a if j%2!=0]
y = []
for w,x in zip(e,o):
    y.append(w)
    y.append(x)
print(y)
'''

for i in range(0,len(a)-1,2):
    a[i],a[i+1]=a[i+1],a[i]
print(a)