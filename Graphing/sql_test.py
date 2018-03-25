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
site = []

q1 = 'SELECT \'Gamespot\', EXTRACT(YEAR FROM Reviewed) as y, ROUND(AVG(SCORE), 2) FROM Gamespot Where EXTRACT(YEAR FROM Reviewed) <> 2018 AND EXTRACT(YEAR FROM Reviewed) >= 2010 GROUP BY y union SELECT \'IGN\', EXTRACT(YEAR FROM Reviewed) as y, ROUND(AVG(SCORE), 2) FROM IGN Where EXTRACT(YEAR FROM Reviewed) <> 2018 GROUP BY y union SELECT \'Polygon\', EXTRACT(YEAR FROM Reviewed) as y, ROUND(AVG(SCORE), 2) FROM Polygon Where EXTRACT(YEAR FROM Reviewed) <> 2018 GROUP BY y union SELECT \'Destructoid\', EXTRACT(YEAR FROM Reviewed) as y, ROUND(AVG(SCORE), 2) FROM Destructoid Where EXTRACT(YEAR FROM Reviewed) <> 2018 AND EXTRACT(YEAR FROM Reviewed) >= 2010 GROUP BY y'

def db(conn, q):
    cur = conn.cursor()
    cur.execute(q)
    i = 0
    for row in cur.fetchall():
        site.append(str(row[0]))
        year.append(int(row[1]))
        score.append(float(row[2]))
        print (str(i) + str(row))
        i += 1
        
myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)

db(myConn, q1)
my_data = {'2010':{site[0]:score[0], site[8]:score[8], site[22]:score[22]},
           '2011':{site[1]:score[1], site[9]:score[9], site[23]:score[23]},
           '2012':{site[2]:score[2], site[10]:score[10], site[24]:score[24], site[16]:score[16]},
           '2013':{site[3]:score[3], site[11]:score[11], site[25]:score[25], site[17]:score[17]},
           '2014':{site[4]:score[4], site[12]:score[12], site[26]:score[26], site[18]:score[18]},
           '2015':{site[5]:score[5], site[13]:score[13], site[27]:score[27], site[19]:score[19]},
           '2016':{site[6]:score[6], site[14]:score[14], site[28]:score[28], site[20]:score[20]},
           '2017':{site[7]:score[7], site[15]:score[15], site[29]:score[29], site[21]:score[21]}}

new_data = {'2010':{site[21]:score[22]},
           '2011':{site[23]:score[23]},
           '2012':{site[24]:score[24]},
           '2013':{site[25]:score[25]},
           '2014':{site[26]:score[26]},
           '2015':{site[27]:score[27]},
           '2016':{site[28]:score[28]},
           '2017':{site[29]:score[29]}}
df = pd.DataFrame(my_data)

axs = df.T.plot(kind='line', figsize=(10,10), fontsize=20)

axs.set_xlabel("Year", fontsize=13)
axs.set_ylabel("Game Score Averages", fontsize=13)
plt.title('Game Score Yearly Trend', fontsize=16)
plt.show()
myConn.close()
    