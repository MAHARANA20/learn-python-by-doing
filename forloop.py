"""
FOR LOOP 
For loop is used to iterate over collection (such as list,tuple,set,dictionary or strings) . 
It is very much similar to other prigramming languages .
"""
#Define a list .
list1=["1","2","3","4"]
list2=["A","B","C","D"]

#for each or for loop
#loop through the list

for x in list1:
    print(x)
    

print ("I am outside for loop ")

#for loop for string 
for x in "PYTHON":
    print(x)

#nested for loop 
for x in list1:
    for y in list2:
        print(x,y)

#Using break in for loop 
for x in list1 :
    print(x)
    if x=="3":
        break

#Using continue in for loop 
for x in list1:
    if x == "3" :
        continue
    print(x)



