#print sum of numbers depending upon the condition

def sum_num(x,value):
    if value=="even" or value=="EVEN":
        print("SUM OF EVEN NUMBERS INCLUDING ",x," IS EQUAL TO => ",sum(range(0,x+1,2)))
        print("SUM OF EVEN NUMBERS EXCLUDING ",x," IS EQUAL TO => ",sum(range(0,x,2)))
    elif value=="odd" or value=="ODD":
        print("SUM OF ODD NUMBERS INCLUDING ",x, " IS EQUAL TO => ",sum(range(1,x+1,2)))
        print("SUM OF ODD NUMBERS EXCLUDING ",x," IS EQUAL TO => ",sum(range(1,x,2)))
    else:
        print("SUM OF NATURAL NUMBERS INCLUDING ",x,"IS EQUAL TO => ",sum(range(x+1)))
        print("SUM OF NATURAL NUMBERS EXCLUDING ",x," IS EQUAL TO => ",sum(range(x)))

a=int(input("Enter the range of the number::::"))
b=input('''Enter the type 
         1) ODD OR odd for sum of odd numbers 
         2) EVEN or even for sum of even numbers 
         3) ANYTHING for sum of n-1 natural numbers:::::''')

sum_num(a,b)
