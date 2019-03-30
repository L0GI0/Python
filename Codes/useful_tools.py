#!/usr/bin/python3

#modules make python awesome language 

#we importing usefull functions we want to use in our programm 
import random

feet_in_mile = 5280
meters_in_kilemeter = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]


def get_file_ext(filename):
	return filename[filename.index(".") + 1]


def roll_dice(num):
	return random.randint(1, num)