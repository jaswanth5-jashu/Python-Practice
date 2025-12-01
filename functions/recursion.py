#factorial number in recursion
'''
def pop(n):
    if n == 0:
        return 1
    else:
        return n*pop(n-1)

print(pop(5))
'''
#generetor nth fibonacci number using recursion

'''
def fin(n):
    if n<=1:
        return n
    return fin(n-1)+fin(n-2)

print(fin(5-1))
'''

#sum of digitd in recursive
'''
def opp(n):
    if n == 0:
        return 0
    return n+opp(n-1)
print(opp(5))    
'''

#print pattern 54321012345
'''
def pattern(n):
    print(n,end='')
    if n == 0:
        return 0
    pattern(n-1)
    print(n,end = '')

    
pattern(5)
'''
#sum of elements in list

'''
n = [1,2,3,4,5,6]

def sumof(n):
    if len(n) == 0:
        return 0
    else:
        return n[0]+sumof(n[1:])

print(sumof(n))
'''

#nested list to single list using recursive
#i/p = [1,[2,3],4,[5],[6,7,8,9],10] | o/p = [1,2,3,4,5,6,7,8,9,10]
'''
def flattenlist(n):
    out = []
    for i in n:
        if type(i) == list:
            out.extend(flattenlist(i))
        else:
            out.append(i)
    return out

n = [1,[2,3],4,[5],[6,7,8,9],10] 
print(flattenlist(n))
'''
#check given number is prime or not

'''
def isprime(n,i=2):
    if n<=1:
        return False
    if i*i>n:
        return 'Prime'
    if n%i == 0:
        return 'Not prime'
    return isprime(n,i+1)
    
print(isprime(5))
'''

#n even numbers by using recursive function
'''
def iseven(n,i=0):
    if n == 0:
        return 
    else:
        print(i,end=' ')
        iseven(n-1,i+2)
        
iseven(5)
'''
#n odd numbers by using recursion function
'''
def isodd(n,i=1):
    if n == 0:
        return 
    else:
        print(i,end=" ")
        isodd(n-1,i+2)
isodd(5)
'''
#sum of digites using recursion function
'''
def sum_digit(n):
    if n == 0:
        return 0
    else:
        return (n%10) + sum_digit(n//10)
print(sum_digit(12345))
'''
