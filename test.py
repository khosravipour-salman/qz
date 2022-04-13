import sqlite3
from sqlite3 import Error

con = None

# try:
con = sqlite3.connect('test_db')
cur = con.cursor()


# does_table_exist_query = 'SELECT name FROM sqlite_master WHERE type="table" AND name="{}";'.format('users')
# res = cur.execute(does_table_exist_query)
# print(res.fetchone())
# con.commit()


# create_table_query = 'CREATE TABLE users ("{}"  INTEGER PRIMARY KEY, "{}" TEXT NOT NULL UNIQUE, "{}" TEXT NOT NULL, "{}" TEXT NOT NULL, "{}" TEXT NOT NULL, "{}" TEXT NOT NULL );'.format(
# 	'user_id', 'username', 'first_name', 'last_name', 'email', 'city'
# )

# cur.execute(create_table_query)
# con.commit()

# insert_query = 'INSERT INTO users ("username", "first_name", "last_name", "email", "city") VALUES( "{}", "{}", "{}", "{}", "{}");'.format(
# 	'test_username1', 'test_first_name', 'test_last_name', 'test@gmail.com', 'test_city'
# )

# cur.execute(insert_query)
# con.commit()



# get_users_query = 'SELECT username, first_name FROM users ORDER BY user_id DESC LIMIT 3;'
# get_users_query = 'SELECT * FROM users;'
# d = cur.execute(get_users_query)

# for i in d.fetchall():
# 	print(i)
# con.commit()

# except Error as e:
# 	print(e)

# finally:
if con:
	con.close()