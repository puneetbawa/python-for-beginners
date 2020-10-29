#Reverse Number Pattern
'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
21
321
4321
'''

rows=int(input())
for i in range(rows+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

