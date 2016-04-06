#!/usr/bin/python

import sqlite3
#set connection to None in case db can't be opened
conn = None

#connect to or create db
conn = sqlite3.connect('scan.db')
print "Opened database successfully"

#create table and columns
conn.execute('''CREATE TABLE ATTENDANCE
    (ID INT PRIMARY KEY     NOT NULL,
    CLASSNO INT     NOT NULL,
    DATE    DATE    NOT NULL,
    SECTION   TEXT);''')
print "Table created successfully"

conn.close()

