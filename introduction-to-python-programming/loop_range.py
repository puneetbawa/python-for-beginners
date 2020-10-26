
''' range(5) is equal to range(0,5) whenver the single parameter is inside the range function, it indicates the terminating condition rather than the intialisation condition. The intialisation in this case automatically defaults to 0. 
range(0,5) intial=0; terminate=5 where 5 is not the part of output, terminating number is not-inclusive of the output
range(0,5,2) initial=0; terminate=5, step_size=2, 0,0+2=2,2+2=4 => 0,2,4 
range(0,6,2) initial

QUES1: The user inputs an integer such that he wants to evaluate the sum of the all the numbers till the entered integer with the entered input as exclusive part of the evaluation 


examples:

INPUT: 5
OUTPUT: 0 1 2 3 4 
        10

TEST CASE1
INPUT: 10
OUTPUT: 0 1 2 3 4 5 6 7 8 9
        45

TEST CASE2
INPUT: 1
OUTPUT: 0 
        0


HW:
INPUT: 5
OUTPUT: 0 1 2 3 4
        6
INPUT: 10
OUTPUT: 0 1 2 3 4 5 6 7 8 9
        20
'''

x=int(input())
for i in range(1,x,2):
    print(i,end=" ")
print()
print(sum(range(1,x,2))) ### 0+1+2+3+4=10
