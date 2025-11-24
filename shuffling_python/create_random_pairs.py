a = ["Alice","Bod","Charlie","David","Eve","Frank","Grace","Hannah"]
import random
random.shuffle(a)
for i in range(0,len(a),2):
    print(a[i],",",a[i+1])
    