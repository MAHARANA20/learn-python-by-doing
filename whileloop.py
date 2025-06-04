"""
While loop in python 

Here while loop is very similar to c,cpp and java 
As always while loop requires pre-defined variable(s)
With the while loop we can execute a set of statements as long as a condition is true .

"""
#Define the while loop 
i=1               #initialisation
while i<10 :      #condition
    print (i)
    i+=1          #increment/decrement

#using break 
print()
i=1
while i<5 :
    print(i)
    if i==3 :
        break 
    i+=1   

#using continue
print()
i=0
while i<5 :
    i+=1
    if i==3 :
        continue
    print(i)

#using else
print()
i=1
while i<5 :
    print(i)
    i+=1
else :
    print("While loop executed successfully.")     
