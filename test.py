import sqlite3

# conn = sqlite3.connect('database.db')
# print('create & connect database')
# conn.execute(
#     '''
#     CREATE TABLE registrants (id INTEGER, name TEXT NOT NULL, sport TEXT NOT NULL, PRIMARY KEY(id));
#     '''
# )
# print('create table')
#
# conn.close()

db = sqlite3.connect('C:/Users/hyang/PycharmProjects/freshIMs/database.db', check_same_thread=False, isolation_level=None)
# db = SQL("sqlite:///froshims.db")
cur = db.cursor()
# cur.execute("CREATE TABLE registrants (id INTEGER, name TEXT NOT NULL, sport TEXT NOT NULL, PRIMARY KEY(id));")
cur.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", ("Mihyang", "Ultimate Frisbee"))
rows = cur.fetchall()
for row in rows:
    print(row)
# cur.execute('select * from registrants')

db.close()