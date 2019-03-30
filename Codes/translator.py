#!/usr/bin/python3

#basic translator 

#Giraffe Language
#vowels -> g (any vowel becomes g)

#------

#dog -> dgg
#cat -> cgt

def translate(phrase):
	translation = ""
	for letter in phrase:
		if letter.lower() in "aeiou":
			if letter.isupper():
			translation = translation + "G"
		else:
			translation = translation + "g"
		else:
			translation = translation + letter
	return translation

print(translate(input("Enter a phrase: ")))

#comments in python 

''' (quotation marks)
asdasd
asdasd
asdasd
asdasd
'''
