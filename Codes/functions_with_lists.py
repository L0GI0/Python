#!/usr/bin/python3

lucky_numbers = [32, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
print(friends)
#append another lists at the end of a list 
friends.extend(lucky_numbers)
print(friends)
#adding indivitual elements at the end of given list
friends.append("Creed")
#adding individual elements at the specific index
friends.insert(1, "Kelly")
#remobing specific element
friends.remove("Jim")
#removing whole list 
friends.clear()
#poping an item from a list, getting rid of the last element
friends.pop()
#checking the existence of a element if it is on the list it give its index 
print(friends.index("Kevin"))
#couting duplicates
print(friends.count("Jim"))
#sorting the list in alphabetical order 
friends.sort()
print(friends)
lucky_numbers.sort();
print(lucky_numbers)
#reversing the list 
lucky_numbers.reverse()
#copying a list, creates a copy of given list 

friends2 = friends.copy()