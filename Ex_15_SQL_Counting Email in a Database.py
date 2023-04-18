import sqlite3

#If the database (emaildb.sqlite) does not exist, then it’ll be created. 
conn = sqlite3.connect('emaildb.sqlite') # creating and connecting to the database
cur = conn.cursor() # similar to file handle

cur.execute('DROP TABLE IF EXISTS Counts') # Droping the table (if it already exists) that we are about to create

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter-')
fh = open(fname)

if len(fname) <0:
    fh = open('mbox.txt')

for i in fh:
    if i.startswith('From:'):
        pieces = i.split()
        email_id = pieces[1]
        domain_name = email_id.split('@')[1]
        cur.execute('SELECT count FROM Counts WHERE org = ?', (domain_name,)) # going to read this like a file or bunch of data # this line doesnt do anything much
        row = cur.fetchone() #row is none when u print coz count column is none from the above code
        if row is None:
            cur.execute('INSERT INTO Counts (org,count) VALUES (?, 1)', (domain_name,))
        else:
            cur.execute('UPDATE Counts SET count = count+1 WHERE org = ?', (domain_name,))


conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), str(row[1]))

cur.close()
