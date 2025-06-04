"""
-> List is a data-structure in python which is mutable or changeable or ordered sequence of elements . 
-> List are just like dynamically sized arrays , similar to vector in c++ and arraysize in Java .
-> Lists need not to be homogeneous always which makes it powerful tool in python . This means a single list may contain Datatypes
   like integer ,strings as well as objects . In other words ,a list can contain diff type of elements .

"""

# Define a list 
list1 = ["A","B","C","D","E"]

# Print the list 
print(list1) 

# Access the elements of list 
print(list1 [3])

# Total no. of elements in list 
print(len(list1))

# Replace an element from list 
list1[3] = "F"
print(list1)

# Find the index no. of elememt 
x = list1.index("C")
print(x)

#Append an element in the list 
list1.append("G")
print (list1)

#Insert an element with a specific index no.
list1.insert(2,"H")
print(list1)

#Loop in the list 
for x in list1 :
    print(x)


# check if the element exist or not 
if "A" in list1:
    print("Yes, A is present")    



