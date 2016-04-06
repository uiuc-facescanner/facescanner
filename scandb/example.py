#!/usr/bin/python

import sqlite3
#set connection to None in case db can't be opened
conn = None

#connect to or create db
conn = sqlite3.connect('scan.db')
print "Opened database successfully"

#create table and columns
conn.execute('''CREATE TABLE STUDENTS
    (ID INT PRIMARY KEY     NOT NULL,
    NAME    TEXT    NOT NULL,
    NETID   TEXT);''')
print "Table created successfully"

#fill columns
conn.execute("INSERT INTO STUDENTS (ID,NAME,NETID) \
      VALUES (1, 'Ben', 'bbchase' )")

conn.execute("INSERT INTO STUDENTS (ID,NAME,NETID) \
    VALUES (2, 'Sarah', 'sarah1' )")

conn.execute("INSERT INTO STUDENTS (ID,NAME,NETID) \
    VALUES (3, 'Greg', 'gregory1' )")

conn.execute("INSERT INTO STUDENTS (ID,NAME,NETID) \
    VALUES (4, 'Alice', 'alice1' )")

conn.commit()
print "Records created successfully"

conn.close()

