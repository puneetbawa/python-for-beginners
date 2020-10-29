#alpha pattern

'''
Print the following pattern for the given N number of rows.
Pattern for N = 3
 A
 BB
 CCC
'''


rows=int(input())
value=65
for i in range(rows):
    for j in range(i+1):
        print(chr(value),end="")
    value+=1
    print()
