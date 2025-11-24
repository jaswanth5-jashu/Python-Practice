x=[1,2,3,4,5]
o=[]
for i in range(len(x)-1,-1,-1):
    o.append(x[i])
print(o)

#m2
print(list(reversed(x)))

#m3
k = []
for j in x:
    k = [j] + k
print(k)

#m4
res = [x[i] for i in range(len(x)-1,-1,-1)]
print(res)

