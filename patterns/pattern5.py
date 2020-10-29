#triangular star pattern

'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
*
**
***
****
'''


rows=int(input())

for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    print()
