#!/usr/bin/python3

number = int(input("Enter a number: ")) # if we dont something different
#than number, error occurs 
print(number)

#try except block 

try: 
	number = int(input("Enter a number: "))
	print(number)
	#value = 10/0 if not specified, exception will caught any error 
	#and still printing out Invalid Input even though it may 
	#be valid 
	#we can store error as a variable
except ZeroDivisionError as err:
	print(err) # here the specific error is printed 
except ValueError:
	print("Invalid Input")