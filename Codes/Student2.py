#!/usr/bin/python3

class Student:
	def __init__(self, name, major, gpa):
		self.name = name
		self.major = major
		self.gpa = gpa 
			#we always have to spend "self" ad 1st parameter 
	def on_honor_roll(self):
		if self.gpa >= 3.5:
			return True 	
		else:
			return False

