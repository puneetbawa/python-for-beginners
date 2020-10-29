#insert at any position 
# with the insert() -> in-built function we can insert one item at a desired location
#                                   or
# insert mutiple items by squeezing it into an empty slice of a list 


list_odd=[1,9,11]
list_odd.insert(1,3) #list_odd[1]=3, then 9 would hav been replaced by 3
print(list_odd)
'''
[1,3,9,11]
list_odd[0]=1
list_odd[1]=3
list_odd[2]=5
list_odd[3]=7
list_odd[4]=9
list_odd[5]=11
'''
list_odd[3:3]=[5,7,13]

print(list_odd)



