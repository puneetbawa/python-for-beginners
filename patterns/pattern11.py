'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
121
1221
'''

rows=int(input())
value=1
print(value)
for i in range(1,rows):
    for j in range(0,i+1):
        if j==0 or i==j:
            print("1",end="")
        else:
            print("2",end="")
    print()
