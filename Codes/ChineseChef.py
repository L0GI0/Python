#!/usr/bin/python3
from Chef import Chef
#instead of copying all this functions we can inherit them
	#classname("name of inherited class")
class ChineseChef(Chef):
	#our chinesechef can do everything that generic chef can do 

	# def make_chicken(self):
	# 	print("The chef makes a chicken")

	# def make_salad(self):
	# 	print("The chef makes a salad")

	#if not overrider a function from default class will be called 
	def make_special_dish(self):
	 	print("The chef makes orange chicken")

	def make_friend_rice(self):
		print("The chef makes a friedrice")