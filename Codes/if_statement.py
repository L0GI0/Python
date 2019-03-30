#!/usr/bin/python3 

is_male = True #boolean value need to begin with uppercase 
is_tall = True 

#key word if or else
if if_male or is_tall:
	#everything it that indentetion will be in the if statement  
	print("You are a male or tall or both")
else:
	print("You neither male or tall")

#and key word
if if_male and is_tall:
	#everything it that indentetion will be in the if statement  
	print("You are a tall male")
else:
	print("You are not tall man")

#else if
#elif, not, key words
if if_male and is_tall:
	#everything it that indentetion will be in the if statement  
	print("You are a tall male")
elif is_male and not(is_tall):
	print("You are a short male")
elif not(is_male) and it_tall:
	print("You are not a male but are tall")
else:
	print("You are not tall man") 