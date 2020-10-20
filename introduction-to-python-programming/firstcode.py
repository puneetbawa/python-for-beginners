#Code 

#Python Variables 

'''
a=10*20/2+4-8
what is the value of a after the program or line of a program is executed?
a) 96
b) 98
c) 102
d) None of the above --> correct answer

associativity-> what is the order of operation/assignment/execuntion: 1) L2R 2) R2L
'''

a=10   #assignment operators carry associativity from R2L  
b=10.2

z=a+b #assignment and arithematic 
print("value of z is:",z)

'''
Step1: assignment operators have associativity from R2L -> i) evaluate Right side ii) assign it to left 
Step2: arithematic operator have associativity left to right but depend upon the rule of precedence
a=1,b=2,c=3,d=4
if i am taking variable y=a*b+c*d = 
	step 2.1:  1*2+3*4 
	step 2.2:  2+3*4
	step 2.3: 2+12
	step 2.4: 14
the output of the step 2 is 14 such that the right side has been successfully evaluated. 
Step3: According step 1, first point is complete i.e. evaluation of right side and now this step will assign the output to left
Finally, the value of 14 is assigned to variable y
Hence, the general solving algorithm for the given operation y is successfully completed
''' 
#---------------------------------------------------------------------------------------####
c='str'
d=a
e=a+2-2
print("Id of a is",id(a))
print("Id of b is",id(b))
print("Id of c is",id(c))
print("Id of d is",id(d))
print("Id of e is",id(e))
#print type of the variables

'''
this is the first python code of batch 2020 that we are 
going to execute such that the class is clear of the variables, types, operators and their basic calculative measures and aspects
this is the first python code of batch 2020 that we are 
going to execute such that the class is clear of the variables, types, operators and their basic calculative measures and aspects
'''
#print("Type of the variable a is:" + a) this line will result into an error due to concatenation of string and integer 

print("Value of the variable a is:", a)
print("Type of the variable a is:", type(a))

print("Value of the variable b is:", b)
print("Type of the variable b is:", type(b))

print("Value of the variable c is:" + c)
print("Type of the variable c is:", type(c))

#find the average of three numbers by taking in the input from the user
'''
till now we have only used asssignment operators for directly interacting with the interpretor/compiler
objective now is to take the desired input from multiple users and enhance the same logic accordingly (Standardised answer for all the platforms)
'''
u=int(input("Enter number 1:"))  #input function is used to take the input from the user end

#also the you can you desired text into the input like: input("Enter number 1:")
#whenever you take input from the user, python by deafult takes it as the string

v=int(input("Enter number 2:"))

w=int(input("Enter number 3:"))
#example u=10,v=20,w=30
avg= (u+v+w)/3
print("average of the number is", avg)
