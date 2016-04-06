#!/usr/bin/python

import sqlite3
conn = None

conn = sqlite3.connect('scan.db')
print "Opened database successfully"

conn.execute("UPDATE STUDENTS set NETID = 'jones1' where ID=4")
conn.commit
print "Total number of rows updated :", conn.total_changes

cursor = conn.execute("SELECT id, name, NETID from STUDENTS")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "NetID = ", row[2], "\n"

print "Operation done successfully"
conn.close()