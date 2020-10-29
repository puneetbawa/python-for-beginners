'''

Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
202
3003
'''

rows=int(input())
value=1
print(value)
for i in range(1,rows):
    for j in range(0,i+1):
        if j==0 or i==j:
            print(value,end="")
        else:
            print("0",end="")
    value=value+1
    print()
        
