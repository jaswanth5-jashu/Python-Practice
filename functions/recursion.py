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

def fab(x):
    return fin(x-1)

print(fab(1))
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

