x = [1,2,3,4,5,6]

for i in range(0,len(x)-1,2):
    x[i],x[i+1]=x[i+1],x[i]
for j in range(0,len(x)-1,2):
    x[j],x[j+1]=x[j+1],x[j]
print(list(reversed(x)))