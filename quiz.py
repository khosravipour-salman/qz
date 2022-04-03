from random import choice
from colored_text import colored_print
from questions import questions as var


def get_questions(limit=10):
	questions = []
	
	counter = 1
	while len(questions) < limit:
		q = choice(list(var.keys()))
		
		if q not in questions:
			questions.append((counter, q))

		counter += 1

	return questions


def ask_questions():
	questions = get_questions()

	user_score = 0
	for count, i in questions:
		colored_print(f'{count}. {i}', 'cyan')
		colored_print('   '.join(var[i]) + '\n', 'message')
		
		user_answer = input('Type in the answer: ')
		if user_answer.lower() in var[i] and var[i][user_answer.lower()]:
			user_score += 1

	colored_print(f'\nYour quiz score is : {user_score}', 'success')
	return user_score