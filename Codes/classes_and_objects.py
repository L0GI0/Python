#!/usr/bin/python3

#not all things can be representent in string, number,
#the datatypes that are build in, usage of class can be used to define
#own created datatype


#from the Student file import Student class
from Student import Student 


student1 = Student("Jim", "Business", 3.1, False)
student1 = Student("Pam", "Art", 4.2, True)
#when object is created _init_ function is called 

#print out the students name
print(student1.name)
#print out the students gpa 
print(student1.gpa)