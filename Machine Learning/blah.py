# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 18:46:50 2018

@author: mustu
"""

import mysql.connector
import numpy as np

publisher = []
developer = []
genre = []
score = []
game = []
new_list = []


def dbRun(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    
    for i in cur.fetchall():
        print i
        #score.append(score)
    cur.close()

hostname = 'game-reviews.cix4c2nzx8tc.us-east-2.rds.amazonaws.com'
username = 'gamers'
password = 'mostharsh'
database = 'GameReviews'

query1 = 'select publisher, genre, developer, score from Gamespot limit 10'
myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
dbRun(myConn, query1)

'''
for i in publisher:
    i = (''.join(i).encode('ascii'))
    print i

print '\n'

for j in developer:
    j = (''.join(j).encode('ascii'))
    print j
print '\n'
'''
"""
for k in genre:
    k = (''.join(k).encode('ascii'))
for i in xrange(len(publisher)):
    publisher[i] = (''.join(publisher[i])).encode('ascii')

for i in publisher:
    print i
"""