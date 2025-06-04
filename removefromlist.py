"""
Remove Item
There are several methods to remove items from list1 list:
1. remove() -Removes specific item .
2. pop(index No) - Removes the specified index .
3. pop() - Removes the last item if index is not specified .
4. Del keyword with given index number deletes specific element .
5. Del keyword without index no. deletes whole list.
6. clear() - empties the list ,  will not delete the list .

"""

# Define a list 
list1 = ["A","B","C","D","E"]
list2 = ["1","2","3","4","5"]

print(list1)

# Using remove()
list1.remove("C")
print(list1)

#Using pop() in index no.
list1.pop(1)
print(list1)

#Using pop() without index no.
list1.pop()
print(list1)

print(list2)

#Using del keyword with index no.
del list2[3]
print(list2)

#Using del keyword without index no.
del list2  #del the wholes list 

#print(list2)

#Using clear 
list1.clear()
print(list1)


