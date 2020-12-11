
FILE IS NAMED LOCATION ON DISK TO STORE INFORMATION.FILES ARE USED TO PERMANENTLY STORE DATA IN A NON-VOLATILE MEMORY (e.g. hard-disk)

three major operations on file:
1)open
2)read or write (perform operation)
3)close

modes of opening a file, 
r-> opens file in a reading mode
w-> opens a file for writing mode / create a new file always
x-> opens a file only for execution mode
a-> opens a file for appending without truncating the contents of the file./ create a new file if it doesn't exists
t-> opens in text mode
b-> open in binary mode
+-> opens a file for updating(reading and writing)

closing a file
close()

r+ -> open the file in both reading and writing mode
b -> is for binary 
r+b -> open the binary file in read or write mode
