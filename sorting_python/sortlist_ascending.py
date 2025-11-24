x = [5,2,7,1,3]
#---------------------------------
print(sorted(x))

#M2--------------------------------

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
print(x)

#M3---------------------------------

x.sort()
print(x)