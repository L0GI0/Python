#!/usr/bin/python3

#creating function in python

#function that says hey to the user 

#key word in python (def) now computer knows that we creating function
#after this line code will be in this function 
def say_hi():
	#this code needs to be  indented (wciety) thats the rule in python
	print("Hello User")

#this is no longer going to be considered as inside the function 
#all the code in the function needs to be inteded 	 

#in order to run function it needs to be called 
#as belowe 
print("Top")
say_hi()
print("Bottom")
say_name("Steve")
say_name_age("Mike", 21)

#we can give informations to a functions "parameters"

def say_name(name):
	print("Hello " + name)

def say_name_age(name, age):
	print("Hello" + name ", you are " + str(age))

#functions with return statement 

def cube(num):
	return num * num * num 
	#we cannont put code after return statement in the function
	#it is out of the function 
print(cube(3))

