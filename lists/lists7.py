#deleting a element from list
# deleting one or more element at same time from list is possible using the keyword del. It can also delete the list entirely. 

list_pri=[1,3,5,7,8,11,13,17,19,23]

del list_pri[4]

print(list_pri)

#[1,3,5,7,11,13,17,19,23]

del list_pri[0:9]

print(list_pri)

del list_pri

print(list_pri)#---->will always result in an error

