# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:15:10 2018

@author: mustu
"""

#https://www.a2hosting.com/kb/developer-corner/mysql/connecting-to-mysql-using-python

import mysql.connector

hostname = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com'
username = 'student'
password = 'cs336student'
database = 'BarBeerDrinker'

def db(conn):
    cur = conn.cursor()
    cur.execute("Select distinct s.beer From bars a, sells s Where a.name = s.bar AND s.price < 5 ")
    
    for beers in cur.fetchall():
        print beers
        

myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
db(myConn)
myConn.close()
    