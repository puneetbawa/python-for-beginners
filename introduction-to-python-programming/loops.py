'''
HIGHLIGHTS of using variable:
a=10  #a -> variable
b=20  #b -> variable
c=30  #c -> variable
a-'6'
print(a)
print(type(a)) #to which in-built class does the variable type/data-type belongs to <class str>

#lists,tuples,sets,dictionaries
'''

#LOOPS -> input-> first_list,calculate length(n),intialisation, range->0,n(condition), print(){]body), update 

list_new=[201,202,203,204,207,209,210,222]

#LANGAUGES -> CAMEL CASING IN VARIABLES NAME 
#listNewOneAssigned 
#print(type(first_list))
#my next target is to add 6 to all values of the list
#my desired output should be -> 207,208,209,210,213,215,216,228

i=0 #denote the position value of list/index

for i in list_new: #i in 201, i in 202 .......... i in 222
    print(i,end=" ")

for i in range(0,len(list_new)-1): #i in 0-> i in 1 ......-> i in 6
    print(list_new[i],end=" ") #list_new[0],list_new[1].........list_new[7]
'''
#functioning loop
step1:i=0,n=8
step2:i<=n(this is not the case for range function of python
        i<n(this is the case for range function of python)
step3:print(list_new[0])
step4:i=1 
    go to step2
    step2: i<n ,i =1
    step3: print(list_new[1])
    step4: i=2
    go to step
'''


























#print(first_list)
#print(len(first_list))

#for i in range(1,3):
#    print(i)


