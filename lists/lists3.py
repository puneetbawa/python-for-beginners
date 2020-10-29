#changing element in a list 
'''
lists are mutable, meaning their elements can be changed unlike string
we can use assignment operator(=) to change an item or a range of items
'''
#correcting mistakes in marks

bhumika=[80,76,92,48,90]
print("previous: ", bhumika)

bhumika[3]=84

print("latest: ", bhumika) #[80,76,92,84,90]

bhumika[1:4]=[82,98,90]

print("after grace: ", bhumika)

