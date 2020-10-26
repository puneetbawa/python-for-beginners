

num=int(input("Enter a number:")) #GETTING AN INPUT FROM USER AND TYPE-CASTING INTO INT
temp=num #INTIALISING A TEMPORARY VARIABLE TO STORE A ENTERED NUMBER
rev=0 #INTILIASING A VARIABLE AS 0 FOR REPETITIVE CALCULATION IN THE LOOP

'''
EXAMPLE 151 number -> palindrome

num=int(input("Enter a number:"))
temp=num 
rev=0

while(num>0):
    dig=num%10= 1
    rev=rev*10+dig
    num=num//10

if(rev==temp):
  print("Palindrome")
else:
 print("Not Palindrome")

ITER1:    dig=151%10=1
          rev=0*10+1=1
          num=num//10=151//10=15
ITER2:    dig=15%10=5
          rev=1*10+5=15
          num=num//10=15//10=1
ITER3:    dig=1%10=1
          rev=15*10+1=151
          num=num//10=1//10=0
if(temp==rev):  151==151 hence->  palindrome number

EXAMPLE 132 number -> not palindrome

ITER1: dig=132%10=2
       rev=0*10+2=2
       num=num//10=132//10=13

ITER2: dig=13%10=3
       rev=2*10+3=23
       num=13//10=1
ITER3: dig=1%10=1
       rev=23*10+1=231
       num=0
'''

while(num>0):                         
    dig=num%10                      
    rev=rev*10+dig
    num=num//10

if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
