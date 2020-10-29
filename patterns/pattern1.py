
rows=6 

for num in range(rows):
    for i in range(num):
        print(num, end=" ")
    print()
'''
Step for num in range(6):
    step1:num=0
          for i in range(0): 0,0
             --------------------- skip
    step2:num=1
          for i in range(1): 0,1
              1
    step3:num=2
          for i in range(2): 0,1,2
              2 2 
    step4:num=3
          for i in range(3): 0,1,2,3
              3 3 3
    step5:num=4
          for i in range(4):
              4 4 4 4
    step6:num=5
          for i in range(5):
              5 5 5 5 5

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

'''
