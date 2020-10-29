#appending and extending lists in python 

list_odd=[1,3,5,7,9]
'''
list_odd[5]=11
print(list_odd)
--> this will run into an error as the index gets out of the range for the specified length of a list
INorder to overcome this erros, one needs to use append() function - in-built function
'''
list_odd.append(11)
list_odd[5]=13 #after appending the length of the list also changes 
print(list_odd) #[1,3,5,7,9,13]

list_odd.extend([15,17,19])
print(list_odd)
