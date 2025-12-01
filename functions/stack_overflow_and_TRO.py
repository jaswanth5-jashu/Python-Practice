#how would you implement basic tail recursion in python

##---------------------------------->here we are performing minimum recursive like condition will stop the recursion using TRO
'''
def tail_recursive(n):
    if n == 0:
        return 0
    else:
        return (n%10) + tail_recursive(n//10)

print(tail_recursive(12345))
'''

#stack overflow occurring without optimization python

##--------------------->stack overflow because we dont use the TRO in it so the function calls it self upto max limit 996
'''
def stack_overflow(n):
    return stack_overflow(n)
print(stack_overflow(1))
'''

#optimize tail recursion with and accumulator in python

###--------------------->here accumulator means varable storing result in it as i storing 
'''
def tro_acc(n,i=0):
    if n == 0:
        return i
    else:
        return tro_acc(n-1,i+n)
print(tro_acc(5))
'''

#fibonacci sequence without optimization

'''
def feb(n):
    if n<=1:
        return n
    else:
        return feb(n-1)+feb(n-2)
print(feb(5))
'''
#stack overflow occur in the deep recursion

'''
import sys
sys.setrecursionlimit(2500)

def deep_re(n):
    if n==0:
        return "ended"
    else:
        return deep_re(n-1)
print(deep_re(2500))
'''

#implement tail recursion in the calculation of a factorial

'''
def fact(n,acc=1):
    if n == 0:
        return acc
    else:
        return fact(n-1,acc*n)
print(fact(5))
'''