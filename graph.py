# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 11:29:46 2018

@author: Mustufa
"""
#https://stackoverflow.com/questions/29498652/plot-bar-graph-from-pandas-dataframe

"""
Graph idea: Get each site, get average for each genre and then graph it using bar
graph to compare the average scores between each site and see which site prefers a 
certain genre over another"
"""

#axs = result[['IGN_Score','Dest_Score']].plot(kind='bar', title='Game Score', figsize=(10,10), fontsize=12)

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

hostname = 'game-reviews.cix4c2nzx8tc.us-east-2.rds.amazonaws.com'
username = 'gamers'
password = 'mostharsh'
database = 'GameReviews'

score1 = []
score2 = []
score3 = []
score4 = []


def dbRun(conn):
    cur = conn.cursor()
    cur.execute("select AVG(i.Score) as ign, AVG(d.Score) as dest from Destructoid d, IGN i where d.name = i.name and i.Genre like '%Fighting%'")
    
    for scores1, scores2 in cur.fetchall():
        score1.append(float(scores1))
        score2.append(float(scores2))

def dbRun2(conn):
    cur = conn.cursor()
    cur.execute("select AVG(i.Score) as ign, AVG(d.Score) as dest from Destructoid d, IGN i where d.name = i.name and i.Genre like '%RPG%'")
    
    for scores1, scores2 in cur.fetchall():
        score3.append(float(scores1))
        score4.append(float(scores2))

myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
dbRun(myConn)
dbRun2(myConn)

my_data = {'Figher':{'IGN':score1[0], 'Dest':score2[0]},
           'RPG':{'IGN':score3[0], 'Dest':score4[0]}}
df = pd.DataFrame(my_data)
axs = df.T.plot(kind='bar', title='Genre Averages', figsize=(10,10), fontsize=12)
axs.set_xlabel("Genre Type", fontsize=12)
axs.set_ylabel("Average Score", fontsize=12)

plt.show()

myConn.close()