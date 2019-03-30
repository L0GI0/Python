#!/usr/bin/python3
num1 = input("Enter a number ")
num2 = input("Enther anothen number ")

result = int(num1) + int(num2) #string by default in python3 
#we need to cast to actually get numbers added 
result = float(num1) + float(num2) #here we can use decimal numbers  

print (result)