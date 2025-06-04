"""
What is tuple?
Tuple is another type of collection such as list .
The differnce is tuple is written with round brackets .
And it is ordered & unchangeable .
That means once tuple is created you cannot change the  values .
This also means once tuple is created you cannot add items to it .
And you cannot remove items from tuple .
But we can delete tuple .

"""

#define a tuple 
tuple1 =("A","B","C","D","E","F","G","A")
print (tuple1)

#access the element using index no.
print(tuple1[3])

#check the no. of elements in tuple 
print(len(tuple1))

#return the no. of times  specific element in tuple
print(tuple1.count("A"))

#return the index no.of given element 
print(tuple1.index("E"))

#loop with tuple 
for x in tuple1:
    print (x)

#check if item exists 
if "B" in tuple1 :
    print("Yes, B is present")   

#another way to create a tuple using a tuple constructor () 
tuple2 = tuple(("A","B","C","D"))
print (tuple2)


