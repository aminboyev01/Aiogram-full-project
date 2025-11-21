import sqlite3
conn=sqlite3.connect("students.db")
cur=conn.cursor()
cur.execute("DROP TABLE IF EXISTS students")
cur.execute('''CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    last_name TEXT,
    age INT,
    grade INT)
''')

conn.commit()
print("jadval yaratildi!")

students=[
    ("shohrux","aminboyev",19,5),
    ("temur","aliyev",17,4),
    ("suxrob","jumayev",25,5),
    ("guli","aminboyeva",21,5),
    ("akbar","aminboyev",19,3)
]

cur.executemany("INSERT INTO students (name,last_name,age,grade) VALUES(?,?,?,?)",students)
conn.commit()
cur.execute("SELECT * FROM students")
rows=cur.fetchall()
for row in rows:
    print(row)

cur.execute("select name from students")
rows=cur.fetchall()
for row in rows:
    print(row)

for row in cur.fetchall():
    print(row)
print("#############################################")
cur.execute('''update students
set name="lool"
where id=1
''')
conn.commit()
print("#############################################")
cur.execute('''select * from students
''' )
for row in cur.fetchall():
    print(row)

cur.execute('''update students set name="daddi" , last_name="jumaniyozov" where id=1''')
conn.commit()
cur.execute('''select * from students
''' )
for row in cur.fetchall():
    print(row)
print("########!1!")
cur.execute('''delete from students where id =1 or id=2''')
conn.commit()
cur.execute('''select * from students
''' )
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()















