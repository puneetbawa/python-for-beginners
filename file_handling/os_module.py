import os

t1=os.getcwd() #fetching the present working directory
print(t1)   #---> present working directory

#os.mkdir("os_folder2") #-----new folder
#os.chdir("./.") #change the location to the specified existing location
print(os.getcwd()) #-----/home/puneet/Desktop
f1=open("osmodule.txt","r") #----file doesn't exist ar /home/puneet/Desktop
print(f1.read()) #---error

print(os.listdir(".."))
os.rmdir("os_folder2")
'''
windows
os.chdir("d:\\")
print(os.getcwd())
'''
