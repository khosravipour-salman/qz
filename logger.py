from datetime import datetime


def log_user_register(username):
	date_time_obj = datetime.now().replace(microsecond=0)

	handler = open('registerations.log', 'a')
	handler.write(f'{username} {date_time_obj}\n')
	handler.close()


def log_user_score(username, user_score):
	date_time_obj = datetime.now().replace(microsecond=0)

	handler = open('user_scores.log', 'a')
	handler.write(f'{username}  {user_score}  {date_time_obj}\n')
	handler.close()