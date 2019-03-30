#!usr/bin/python3

#opening a file 
#open("filename", "mode") 
#modes :
# r - read
# w - write
# a - append
# r+ - read and write 
employee_file = open("employees.txt", "r")

#printing form a file 
#it's good to check if file is even readable
print(employee_file.readable()) # false if for example read mode is w 

print(employee_file.read()) #spits out of the information in the file 
#printing 2 first lines
print(employee_file.readline()) #reads one line and moves curson to the next line 
print(employee_file.readline()) #reads one line and moves curson to the next line 

#takes each line an put it inside list 
print(employee_file.readlines()[1]) #gives second line of the file 

#printing whole file with for loop and readlines()
for emplyee in employee_file.readlines():
	print(emplyee)

#after opeing a file it needs to be closed

employee_file.close()
