"""
Type casting : FORCEFUL conversion of one data type into another .
"""

a= 1
b= 2.5
c= "3"

print(a)
print(b)
print(c)

d=int (c) # convert the string into integer 
print(d)

e=a+d # performs addition 
print(e)

f=int(b)  #convert the float into int -> 2 instead of 2.5
print(f)

g=float(a) #convert integer into float 
print(g)

h=str(a)
i=c+h # performs concatenation
print(i)

print("A = " + str(a) )