#!/usr/bin/python3

employee_file = open("employees.txt", "a") #appending to the file mode 

#we need \n excape character of a new line in order to add in the new line
employee_file.write("\nKelly - Customer Service")

employee_file.close()


# employee_file = open("employees.txt", "w") #write to file mode


# employee_file.write("\nKelly - Customer Service") #thats going to override whole file 

# employee_file.close()

#creating new file ( we can create for example HTML file)

employee_file = open("index.html", "w")

employee_file.write("<p> This is HTML </p>")

employee_file.close()