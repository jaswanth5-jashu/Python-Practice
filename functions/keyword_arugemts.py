#keyword arugmunets

def key_func(name,age):
    return f"my name is {name} age is {age}"
print(key_func(name = 'jashu',age = 21))

#keyword aruguments with default 

def key_fun(name,age):
    return f"my name is {name} age is {age}"
print(key_fun(name='shiv',age = 24))

#keyword argument validation

def key_func(name,age):
    if age >= 18:
        return f"{name} eligible for vote"
    else:
        return f"{name} not eligible of vote because {age}<18"
print(key_func('jashu',18))

#use multible keyword argumensts

def key_func(a,b,c):
    return a+b+c

print(key_func(a=2,b=2,c=2))
