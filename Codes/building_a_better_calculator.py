#!/usr/bin/python3

#in python no matter what input it always will be
#converted to string 

#with float() will give float number 
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
	print(num1 + num2)
elif op == "-":
	print (num1 - num2)
elif op == "/":
	print(num1 / num2)
elif op == "*":
	print(num1 * num2)
else: 
	print("Invalid operator")






