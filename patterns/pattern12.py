'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
1234
123
12
1
'''


rows=int(input())
n=rows
for i in range(rows):
    value=1
    for j in range(n,0,-1):
        print(value,end="")
        value=value+1
    n=n-1
    print()
