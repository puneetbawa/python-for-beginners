########INPUT 12      
########OUTPUT 24

#######INPUT 24
#######OUTPUT 48

'''
HAS TO BE DONE FUNCTION


def double_value(num):
    #print(num*2)
    return num*2

a=int(input())
b=double_value(a)  #a=12,then value of function has returned(is now set to) num*2, thus double_value(a)=12
print(b)

##double_value(a)=func()

a=int(input())
b=lambda a:print(a*2)         #right side returns function so the left side becomes function, this is called closure function ::::a=12
b(a)               #when i am calling the closure function, that is vreated in the previous step
                       #so now the compiler has reached to return a*2, now this expression b(a) has integer value, b(a)=24
'''

a=int(input())
lambda a:print(a*2)
_(a)
