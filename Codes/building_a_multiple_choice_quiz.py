#!/usr/bin/python3
from Question import Question

question_prompts = [
	"What color are apples? \n (a) Read/Green\n(b) Purple\n(c) Orange \n\n",
	"What color are Bananas?\n(a) Teal\n (b) Magenta\n (c) Yellow \n\n",
	"What color are strawberries? \n (a) Yellow \n (b) Red \n (c) Blue \n\n"	
	]

questions = [
	Question(question_prompts[0], "a"),
	Question(question_prompts[1], "c"),
	Question(question_prompts[2], "b"),
]

#function to loop through the questions
def run_test(questions):
	score = 0
	for quesiton in questions:
		answer = input(question.prompt())
		if answer == question.answer:
			score += 1
	#in order to print we need to cast number to string 
	print("You got" + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)

