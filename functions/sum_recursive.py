#program to compute sum of n natural numbers using recursion

def sum_recursive(num):
    if(num!=0):
        return num + sum_recursive(num-1)
    else:
        return num

x=int(input("Enter the number:"))
total=sum_recursive(x)
print(total) #can also be written as print(sum_recursive(x))

