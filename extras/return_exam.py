#scope example global
#---example---
'''
example 1
a=14 #global scope
def f():
    "local scope"
    global a #re-intiliasing the value of a and referring it to be as global
    a=12 #new value of global a is 12 which is applicable inside scope as well as outside scope as of now
f()
print(a)
'''

#example 2
def function(a,b,c=1,d=7): #definition/initialisation of particular variable is being done in the parameters of the function
    print(c)
    return a+b+c+d

'''
steps-> a=10,b=12,c=5 return 10+12-5=17
'''
value = function(10,12,5)
print(value)

