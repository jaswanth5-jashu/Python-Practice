s= "hello"
i = 1
j = 3
l = list(s)
l[1],l[3]=l[3],l[1]
print("".join(l))