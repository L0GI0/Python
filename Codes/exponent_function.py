#!/usr/bin/python3

#exponent function in python 
print(2**3) #2^3


#we crating our exponent function 

def raise_to_power(base_num, pow_num):
	result = 1
	for index in range(pow_num):
		result *= base_num
	return result



print(raise_to_power(3, 2))