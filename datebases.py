import sqlite3
conn = sqlite3.connect("base.db")

cur = conn.cursor()

params = [
    (4, 'MA', 50),
    (4, 'Prog', 40),
    (4, 'LA', 30),
    (5, 'MA', 80),
    (6, 'Prog', 85)
]

cur.execute('''SELECT students.name
FROM students
WHERE exists (select * from results
where results.ball > 20 and results.studid = students.id)
''')

for f in cur.fetchall():
    name = f
    print name

conn.close()
