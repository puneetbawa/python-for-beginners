import random

#seed function of random

#seed fucntion is used to initialise the psuedorandom number generator in python
#radnom module uses the seed value as a base to generate a random number. 
#If seed value is not present,it takes a current time 
#if you use the same seed value befrore calling any random module function, you will get the same output every time

#random.seed(4)
print(random.randint(10,20))

print(random.randint(3,20))

#shuffle 

l1=[2,4,5,7,8,10,11,12,14,1,3]
print(l1)
random.shuffle(l1)
print("Shuffled List",l1)


#to generate a floating type number within a given range

print("floating point within a given range")
print(random.uniform(10,24))

print("integer within a given range")
print(random.randint(10,24))
