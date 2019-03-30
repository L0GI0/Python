#!/usr/bin/python3
#dictionary - slownik 

#the key correspond to the word in normal dictionary 

#e.g
#Jan -> January
#Mar - March

#we define key and we give it corresponding value 
# "(key)": "(value)", they have to be unique
monthConversions = {
	"Jan": "January",
	"Feb": "February",
	"Mar": "March",
	"Apr": "April",
	"May": "May",
	"Jun": "June",
	"Jul":  "July",
	"Aug": "August",
	"Sep": "September",
	"Oct": "October",
	"Nov": "November",
	"Dec": "December",
}

monthConversionsNumbers = {
	1: "January",
	2: "February",
	3: "March",
	4: "April",
	5: "May",
	6: "June",
	7:  "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December",
}
#they are different way of accesing keys
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
#with get() we can specifie a default value if key is not found
#by default it is "none"
print(monthConversions.get("Dec", "Not a valid Key"))
