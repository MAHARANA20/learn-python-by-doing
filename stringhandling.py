#string handling 

a = "Hello, world!"
print (a)

print(len(a))  # Print the length of string , returns no. of characters in string 
print(a[1])    # Returns the character of given index no. 
print(a[2:5])  # Returns the substring with start index no. and end index no. 

print(a.split(",")) #seperates the string with given delimeter 
b = "As per survey its 62 percentage better with live instructor"
print(b.split(" "))

c = "   Hello world!   "
print (c) 
print(c.strip())  #Remove prefixes and postfixes whitespaces 

print(a.replace("H","y") ) #Replaces the old character with new character 
print(a.replace("o","u") )

print(a.lower())   # Convert string into small letters 
print(a.upper())   # Convert string with capital letters


