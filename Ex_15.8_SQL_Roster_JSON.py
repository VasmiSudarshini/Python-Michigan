import sqlite3
import json

conn = sqlite3.connect('RosterJSON.sqlite')
cur = conn.cursor()

#Dropping tables that already exists
cur.executescript('''DROP TABLE if exists User;
DROP TABLE if exists Course;
DROP TABLE if exists Member''')

cur.executescript('''CREATE TABLE User (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                   name TEXT UNIQUE);
CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                     title TEXT UNIQUE);
CREATE TABLE Member (user_id INTEGER, 
                     course_id INTEGER,
                     role INTEGER,
                     PRIMARY KEY(user_id, course_id))''')

filename = input('Enter File name:')
fh = open(filename).read()

if len(filename) <1 :
    file = 'roster_data.json'

data = json.loads(fh)
for list in data:
    
    #picking out the user from the list and populating User table
    user = list[0]
    cur.execute('INSERT OR IGNORE INTO User(name) VALUES (?)', (user,))
    cur.execute('SELECT id FROM User WHERE name = ?', (user,))
    user_id = cur.fetchone()[0]

    #picking out the course from the list and populating Course table
    course_title = list[1]
    cur.execute('INSERT OR IGNORE INTO Course(title) VALUES(?)', (course_title,))
    cur.execute('SELECT id FROM Course WHERE title =?', (course_title,))
    course_id = cur.fetchone()[0]

    ##picking out the role from the list and populating Member table
    role = list[2]
    cur.execute('INSERT OR IGNORE INTO Member(user_id, course_id, role) VALUES (?,?,?)', (user_id,course_id, role))

conn.commit()

sql_str = cur.execute('''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1''')

for row in sql_str:
    print(str(row[0]))
