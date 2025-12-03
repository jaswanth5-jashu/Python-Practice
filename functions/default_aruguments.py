#define a function with default aruguments

def def_fun(a,b=8):
    c = a+b
    return c
print(def_fun(2))

#multiple default values

def def_func(a=2,b=4):
    c = a+b 
    return c
print(def_func())

#handle list in default aruguments

def def_func(i,j=None):
    if j is None:
        j=[]
        j.append(i)
        return j
print(def_func(1))

#handle none with default in mutable objects to avoid iusses

def func(i,j=None):
    if j is None:
        j=[]
        j.append(i)
        return j
print(func(5))