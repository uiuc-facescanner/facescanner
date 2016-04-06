#!/usr/bin/python

import sqlite3

def initDb():
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


def newTable():
    # set connection to None in case db can't be opened
    conn = None

    # connect to or create db
    conn = sqlite3.connect('scan.db')
    print "Opened database successfully"

    # create table and columns
    conn.execute('''CREATE TABLE ATTENDANCE
        (ID INT PRIMARY KEY     NOT NULL,
        CLASSNO INT     NOT NULL,
        DATE    DATE    NOT NULL,
        SECTION   TEXT);''')
    print "Table created successfully"

    conn.close()


def getRecords():
    conn = None

    conn = sqlite3.connect('scan.db')
    print "Opened database successfully"

    cursor = conn.execute("SELECT id, name, NETID from STUDENTS")
    for row in cursor:
        print "ID = ", row[0]
        print "NAME = ", row[1]
        print "NetID = ", row[2], "\n"

    print "Operation done successfully"
    conn.close()


def updateRecord(recordID, newNetID):
    conn = None

    conn = sqlite3.connect('scan.db')
    print "Opened database successfully"

    #conn.execute("UPDATE STUDENTS set NETID = 'jones1' where ID=4")
    conn.execute("UPDATE STUDENTS set NETID=? where ID=?", (newNetID, recordID))
    conn.commit
    print "Total number of rows updated :", conn.total_changes

    cursor = conn.execute("SELECT id, name, NETID from STUDENTS")
    for row in cursor:
       print "ID = ", row[0]
       print "NAME = ", row[1]
       print "NetID = ", row[2], "\n"

    print "Operation done successfully"
    conn.close()


def addRecord(newID, newName, newNetID):
   conn = None

   conn = sqlite3.connect('scan.db')
   print "Opened database successfully"

   conn.execute("INSERT INTO STUDENTS VALUES (?, ?, ?)", (newID,newName,newNetID))

   cursor = conn.execute("SELECT id, name, NETID from STUDENTS")
   for row in cursor:
      print "ID = ", row[0]
      print "NAME = ", row[1]
      print "NetID = ", row[2], "\n"

   print "Operation done successfully"

   conn.close()


def deleteRecords(recordID):
    conn = None

    conn = sqlite3.connect('scan.db')
    print "Opened database successfully"

    conn.execute("DELETE from STUDENTS where ID=;")
    conn.commit
    print "Total number of rows deleted :", conn.total_changes

    cursor = conn.execute("SELECT id, name, NETID from STUDENTS")
    for row in cursor:
        print "ID = ", row[0]
        print "NAME = ", row[1]
        print "NetID = ", row[2], "\n"

    print "Operation done successfully"
    conn.close()


