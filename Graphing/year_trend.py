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

ign_score = []
gamespot_score = []
dest_score = []
poly_score = []

def db(conn):
    cur = conn.cursor()
    cur.execute("""SELECT 'Gamespot', EXTRACT(YEAR FROM Reviewed) as y, ROUND(AVG(SCORE), 2) FROM Gamespot Where EXTRACT(YEAR FROM Reviewed) 
                <> 2018 AND EXTRACT(YEAR FROM Reviewed) >= 2010 GROUP BY y union SELECT 'IGN', EXTRACT(YEAR FROM Reviewed) as y, 
                ROUND(AVG(SCORE), 2) FROM IGN Where EXTRACT(YEAR FROM Reviewed) <> 2018 GROUP BY y union SELECT 'Polygon', 
                EXTRACT(YEAR FROM Reviewed) as y, ROUND(AVG(SCORE), 2) FROM Polygon Where EXTRACT(YEAR FROM Reviewed) <> 2018 
                GROUP BY y union SELECT 'Destructoid', EXTRACT(YEAR FROM Reviewed) as y, ROUND(AVG(SCORE), 2) FROM IGN Where 
                EXTRACT(YEAR FROM Reviewed) <> 2018 GROUP BY y""")
    
    for gamespot, ign, poly, dest in cur.fetchall():
        gamespot_score.append(gamespot)
        ign_score.append(ign)
        poly_score.append(poly)
        dest_score.append(dest)
             
myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
db(myConn)
my_data = {'2010':{'IGN':score[0], 'Dest': dest_score[0], 'Gamespot': gamespot_score[0]}, 
           '2011':{'IGN':score[1], 'Dest': dest_score[1], 'Gamespot': gamespot_score[1]},
           '2012':{'IGN':score[2], 'Dest': dest_score[2], 'Gamespot': gamespot_score[2]},
           '2013':{'IGN':score[3], 'Dest': dest_score[3], 'Gamespot': gamespot_score[3]},
           '2014':{'IGN':score[4], 'Dest': dest_score[4], 'Gamespot': gamespot_score[4]},
           '2015':{'IGN':score[5], 'Dest': dest_score[5], 'Gamespot': gamespot_score[5]},
           '2016':{'IGN':score[6], 'Dest': dest_score[6], 'Gamespot': gamespot_score[6]},
           '2017':{'IGN':score[7], 'Dest': dest_score[7], 'Gamespot': gamespot_score[7]}}
df = pd.DataFrame(my_data)

axs = df.T.plot(kind='line', figsize=(10,10), fontsize=12)
axs.set_xlabel("Year", fontsize=13)
axs.set_ylabel("Game Score Averages", fontsize=13)
plt.title('Game Score Yearly Trend', fontsize=16)
plt.show()
myConn.close()
    