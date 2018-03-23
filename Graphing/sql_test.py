# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:15:10 2018

@author: Mustufa
"""

#https://www.a2hosting.com/kb/developer-corner/mysql/connecting-to-mysql-using-python

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

hostname = 'game-reviews.cix4c2nzx8tc.us-east-2.rds.amazonaws.com'
username = 'gamers'
password = 'mostharsh'
database = 'GameReviews'

year = []
score = []
price = []

def db(conn):
    cur = conn.cursor()
    cur.execute("SELECT extract(YEAR FROM Reviewed) as y, AVG(Score) FROM IGN group by y")
    
    for beers, bars in cur.fetchall():
        year.append(float(beers))
        score.append(float(bars))
        
myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
db(myConn)
my_data = {'2010':{'IGN':score[0], 'Dest': destScore[0]},
           '2011':{'IGN':score[1]},
           '2012':{'IGN':score[2]},
           '2013':{'IGN':score[3]},
           '2014':{'IGN':score[4]},
           '2015':{'IGN':score[5]},
           '2016':{'IGN':score[6]},
           '2017':{'IGN':score[7]},}
df = pd.DataFrame(my_data)
print(my_data)

df.T.plot(kind='line')
plt.show()
myConn.close()
    