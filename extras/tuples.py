#list creation: lists hold a sequence of values just like string holds a sequence of characters
#list is easy to create 

list1=['op',2,4.60,'test']
print(list1)
print(list1[2])

#tuples: sequence of value like list[much like a list]. THe value stored in tuple can be of any type, and they are indexed by integers

tup=()
tup_int=(1,2,3)
tup_mix=('op',2,4.60,'test')

print(tup)
print(tup_int)
print(tup_mix)


#tuples are immutable means we can't change the elements of tuple once it is assigned whereas in the case of list, the elements can be changed

print(tup_mix[2])
#tup_mix[2]=4 ----------> it results into an error for tuple not able to hold nay assignment opertion after the intialistion and declaration

'''
sets: 1) sets are unordered 
      2) set elements are unique. Duplicacy is not allowed
      3) a set itself may be modified, but the elemetns contained in the set must be of an immutable type
      4) sets are used to perform matherical set operations like union, intersection, symmetric difference etc. 

'''

se={1,2,3,3,4,5}
print(se)

list1=['go','go','go','lop','lkj','go']
x=set(list1)
#x=set(['go','go','go','lop','lkj','go'])
print(x)

y=frozenset(list1)
print(y)







































