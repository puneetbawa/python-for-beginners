import random


print("Generating random number using random() function : ", random.random())

#random is the most basic function of random module 
#almost all functions of random depend upon the basic function of random()
#the value of random() function ranges from [0.0,1.0) and always return floating-point number 

#generate the integer radom number between the given range random.randint(a,b)

print("Generating a random integer using randint() function ", random.randint(0,9))

#random.randrange(start,stop,[step])

print("Generating a random integer using randrange() function ", random.randrange(0,20,5))

indian_city=['Mumbai','Hyderabad','Mysore','Gurgaon','Shimla','Chopta']

print("Random element from list using choice() function", random.choice(indian_city))

print("Pick k number of random elements from list using sample() function ", random.sample(indian_city,3))

print("Pick k number of random elements from list using sample() function ", random.sample(indian_city,6))


#random.choices()

list1=[10,20,40,20,30,50,60]
sample=random.choices(list1,k=2)
print("sampling with choices method ", sample)



