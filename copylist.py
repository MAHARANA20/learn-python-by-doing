"""
How to copy a list ?
We cannot copy list1 simply by typing list2=list1
because list2 will only be the list1 reference to list1,
and changes made in list1 will automatically also be made in list2

There are ways to make list copy , list methods :
1.copy()method
2.list()constructor

"""
# Define a list 
list1 = ["A","B","C","D","E"]
print(list1)

#Using copy ()
list2 = list1.copy()
print(list2)

# Using list constructor 
list3 = list(list1)
print(list3)

