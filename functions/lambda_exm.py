'''

>>> def identity(x):
...     return x

>>> lambda x: x

In the example above, the expression is composed of:



The keyword: lambda
A bound variable: x
A body: x

'''

lambda x: x + 1

'''
Reduction is a lambda calculus strategy to compute the value of the expression. 
In the current example, it consists of replacing the bound variable x with the argument 2:

(lambda x: x + 1)(2) = lambda 2: 2 + 1
                     = 2 + 1
                     = 3

'''

add_one = lambda x: x + 1
add_one(2)

lambda x, y: x + y
_(1,2)

(lambda x, y: x + y)(2, 3)




