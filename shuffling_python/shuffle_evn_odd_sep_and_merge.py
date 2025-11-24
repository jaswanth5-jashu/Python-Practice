import random
a  = [1,2,3,4,5,6,7,8,9,10]

even = [i for i in a if i%2 == 0]
odd = [j for j in a if j%2!=0]

random.shuffle(even)
random.shuffle(odd)

r = []
for e,o in zip(even,odd):
    r.append(e)
    r.append(o)
print(r)