x = ['apple','banana','orange','grape','pear']
#----------------------------------------------

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if len(x[i])>len(x[j]) or ord(x[i][0])>ord(x[j][0]):
            x[i],x[j]=x[j],x[i]
print(x)