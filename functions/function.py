#write a funtio without passing aurguments 
'''
def display():
    print('hello world')

display()
'''
#write function with parameter
'''
def display(a):
    return a

a = 'hello'
print(display(a))
'''

#default parameter
'''
def display(a=1,b=3):
    return a+b

a = 1
print(display(a))
'''

#write with docstring and write program

'''
def display(a):
    #this is name
    return a
print(display('ok'))
'''
#-----------------------------------
#local scope
'''
y=2 #global scope
def display():
    x = 1 #local scope
    return x+y

print(display())
'''

#enclosing/non-local scope
'''
x=2
def display():
    y = 1 #non local
    def osm():
        return x+y
    return osm()
    
print(display())
'''
        
#global scope
'''
x = 2 #global
def display():
    return x

print(display())
'''
#Modifying and Accessing Variables
#modify global with in the function 
'''
x=10
def function():
    global x
    x=20
    return x
    
print(function())
'''
#access global var within the function 
'''
x = 10
def function():
    return x

print(function())
'''

#modify non loacl var within the function
'''
x = 10
def outer():
    global x
    x = 100
    y = 10
    def inner():
        nonlocal y
        #y = 50
        return x+y
    return inner()

print(outer())
'''
#12.access a non local varable in a nested function 
'''
def out():
    y = 10
    def inner():
        nonlocal y
        y  = 100
        return y
    return inner()

print(out())
'''
#lambda funtion to square
'''
s = lambda x:x*2
print(s(2))

res = list(map(lambda x:x*2,[1,2,3,4,5]))
print(res)
'''
#add two numbers in python 
'''
res = lambda a,b:a+b
print(res(1,2))
'''
#max of 2 numbers
'''
res = lambda a,b:a if a>b else b
print(res(1,2))
'''
#check if num is even
'''
res = lambda a: 'even' if a%2==0 else 'odd'
print(res(3))
'''
#last digit from the string
'''
res = lambda a:a[-1]
print(res('hello')) 
'''
#to sort list of tuple based on the second element
'''
x = [(2, 9), (4, 3), (1, 7)]
x.sort(key=lambda c:c[1])
print(x)
'''
#use filter even numbers from list
'''
x = [1,2,3,4,5,6,7,8]
res = filter(lambda i:i%2==0,x)
print(list(res))
'''
#lambda with conditional expression to categorize ages
'''
res = lambda a:'minor' if a<18 else 'major'
print(res(17))
'''
#lambda with conditional expression to calculate the factorial of a number using recursion
'''
res = lambda n: 1 if n==0 else n*res(n-1)
print(res(5))
'''
#filter even 
'''
res = filter(lambda i:i%2==0,[1,2,3,4,5])
print(list(res))
'''
#square numbers
'''
res = map(lambda i:i**2,[1,2,3,4,5])
print(list(res))
'''
#simple calculator
'''
add = lambda a,b:a+b
sub = lambda a,b:a-b
mult = lambda a,b:a*b
div = lambda a,b:a/b if b!=0 else 'cannt divide zero'

a = 10
b = 2

print(div(a,b))
'''
#sorting elements 
'''
x = [5,7,1,3,5,8,3]
x.sort(key=lambda i:i)
print(x)

res = sorted(x,key=lambda i:i)
print(res)
'''
#remove duplicates
'''
x = [1,2,3,2,3,4,5,5,6,7]
s = []

res = filter(lambda i: not (i in s or s.append(i)),x )
print(list(res))
'''
#combine list ele wise
'''
x = [1,2,3,4]
y = [5,6,7,8]

res = map(lambda a,b:(a,b),x,y)
print(list(res))
'''
x = [1,2,3,4]
y = [5,6,7,8]

res = map(lambda a,b:[a,b],x,y)
print(list(res))






    

    