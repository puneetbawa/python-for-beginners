
ss="test PUNEET"
print("Upper Case=",ss.upper())
print("Lower Case=",ss.lower())
print("FIrst array=",ss[1:])
#ss=1
#print("Upper Case=",ss.upper())
#BOOLEAN METHODS USED IN STRING 

print("45"+"12")

num="45"
let="qwertyuiop"

print(num.isnumeric())
print(let.isnumeric())


movie="2001: A SAMMY ODYSSEY"
book="Harry Porter And Goblet Of Fire."
poem="the road not taken by robert frost"

print(poem.islower())
print(movie.isupper())
print(book.istitle())

print(len(book))


#join(),split(),replace()


exm="marks have been have uploaded."

print(" ".join(exm))

print(" ".join(reversed(exm)))



print(";".join(["apple","banana","carrot"]))
print("Original string=",exm)
print("Joining for the string class type="," ".join(exm))
print("Joining for the reversed string class type="," ".join(reversed(exm)))
print("Using split function for converting str to list of str=",exm.split())
print("Joining for each word after spliting and converting back to string",";".join(exm.split()))
print("Spliting the given exm string by character v=",exm.split("v"))


print(exm.replace("have","had"))



print("My name is %s and age is %d!" % ('Puneet',26))

para_graph="""

tahthalktjaaknana;kj;ajk;aj;aja;ja;jagiaygrkabrla
ahahglagangakgnaghaoghaogahgnagna
ahgglaghalgnalgalgalghalgalghalhglahgalhglhaglha
ajgagagalghalghlahglahga


"""

print(para_graph)

#print C:\xyz

print("C:\\\\xyz")

print(r"C:\xyz")

exm1="abvdde1"
print(exm1.isalpha())
print(exm1.isalnum())
print(exm1.isdigit())

exm2=" "

print(exm2.isspace())
















