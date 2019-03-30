#!/usr/bin/python3

#while loop

i = 1

while i <= 10:
	print(i)
	i += 1

print("Done with loop")


#for loop 
friends = ["Jim", "Karen", "Kevin"]
len(friends) #number of elements in the array, length of the array
#for every letter we want to do something 
#looping through strings 
for letter in "Giraffe Academy":
	print(letter)

for friend in friends:
	print(friend)
#looping through numbers 

for index in range(10):
	print(index)

for index in range(3,10):
	print(index)


for index in range(len(friends)):
	print(friends[index])

for index in range(5):
	if index == 0:
		print("first Iteration")
	else:	
		print("Not first")




