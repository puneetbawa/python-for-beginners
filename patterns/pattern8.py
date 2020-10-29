###character pattern#####
'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
A
BC
CDE
DEFG

'''


rows=int(input())

for i in range(rows):
    ch=ord('A')+i
    for j in range(i+1):
        print(chr(ch+j),end="")
    print()
