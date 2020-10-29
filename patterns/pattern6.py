#Triangle Number Pattern
'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
22
333
4444
'''

rows=int(input())
for i in range(rows+1):
    num=i
    for j in range(i):
        print(num,end="")
    print()
