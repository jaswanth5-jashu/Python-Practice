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