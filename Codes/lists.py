#!/usr/bin/python3

#list variable
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends = ["Kevin", 2, False] #python is fine with different types of variables

#we can print the actual list 
print(friends)
#printing specific element 
#first element
print(friends[0])
#second
print(friends[1])
#third
print(friends[2])

#using negitive values it starts indexing from the last 
#last (not -0)!!!!!
print(friends[-1])
#beofre last 
print(friends[-2])

#printing list in given range 

print(friends[1:3])

#modyfing element 

friends[1] = "Mike"
print(friends[1])

