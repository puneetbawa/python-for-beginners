#Interesting Alphabets
'''
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE
'''

rows=int(input())
value=65+rows-1
for i in range(rows):
    for j in range(i+1):
        print(chr(value-i+j),end="")
    print()
