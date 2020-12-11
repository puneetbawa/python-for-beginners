f=open("xyz.bin","wb")
num=[5,10,20,30,40,50]
ar=bytearray(num)
f.write(ar)
f.seek(0)
f1=open("xyz.bin","rb")
print(f1.read())
f1.seek(0)
z=list(f1.read()) #iterate binary file into list of choice
print(z)

f.close()
