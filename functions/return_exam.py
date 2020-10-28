'''
code showcases the parameter intilisation in the definition of function 
differnt parameters in the definiation and calling when parameter intiliasation is done during the runtime
'''

a=14
def f():
    global a
    a=12
f()
print(a)

def function(a,b,c=1):
    return a+b-c
value = function(10,12)
print(value)

def function(a,b,c=1):
    return a+b-c
value = function(10,12,5)
print(value)

def function(a,b,c=1,d=5):
    return a+b+c+d
value = function(1,2,d=7)
print(value)
