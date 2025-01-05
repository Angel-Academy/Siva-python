import sqlite3
conn=sqlite3.connect('user.db')
cur=conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS result(
user_id TEXT NOT NULL PRIMARY KEY,roll_no INTERGER NOT NULL,mark REAL NOT NULL)''')
"""
cur.execute('''
INSERT INTO result(user_id,roll_no,mark)VALUES("siva1",20,100)''')
cur.execute('''
INSERT INTO result(user_id,roll_no,mark)VALUES("ram1",20,10)''')
cur.execute('''
INSERT INTO result(user_id,roll_no,mark)VALUES("prem",21,80)''')
cur.execute('''
INSERT INTO result(user_id,roll_no,mark)VALUES("kumar",22,40)''')
cur.execute('''
INSERT INTO result(user_id,roll_no,mark)VALUES("gokul",23,70)''')
cur.execute('''
INSERT INTO result(user_id,roll_no,mark)VALUES("mani",24,55)''')
conn.commit()
"""
cur.execute('''
SELECT * FROM result ''')
details=cur.fetchall()
for i in details:
    print(i)
cur.execute('''
UPDATE result SET mark=10 WHERE user_id="siva1"''')
cur.execute('''
DELETE FROM result WHERE user_id="mani"''')
#cur.execute('''
#drop result
conn.commit()
cur.execute('''
SELECT * FROM result ''')
details=cur.fetchall()
for i in details:
    print(i)
conn.close()
